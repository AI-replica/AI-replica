from functools import reduce
import json
from ntpath import join
from typing import Dict, List
import uuid
import requests
from sanic import Request
import sanic.response as response
from ai_replica.common import get_answer
import server.data_access.data_access as data_access
from server.utils.read_config import config

BOT_ENGINE = config["bot_engine"]
RASA_REST_WEBHOOK = config["rasa"]["rest_webhook"]
TEXT_TO_SPEECH_ACTIVATED = config["server"]["text_to_speech_activated"]
TEXT_TO_SPEECH_ENGINE = config["server"]["text_to_speech_engine"]


def get_response(request: Request, context):
    obj = request.json
    user_message = obj["message"]
    data_access.add_message(
        user_message, context["user_id"], context["conversation_id"]
    )

    # TODO: provide engine logic via a strategy, e.g. implement a separate class/function to process Rasa requests
    if BOT_ENGINE == "rasa":
        url = RASA_REST_WEBHOOK
        # the value of the sender field corresponds to the conversation id in rasa conversation store
        data = {
            "sender": context[
                "user_id"
            ],  # TODO: add user management logic: authentification, etc.
            "message": user_message,
        }
        rasa_response = requests.post(url, data=json.dumps(data))
        bot_answers = __get_bot_answers_from_rasa_bot_answers(rasa_response.text)
    else:
        bot_answers = [get_answer(user_message)]

    guid = str(uuid.uuid4())
    content = {"messages": bot_answers, "guid": guid}
    data_access.add_message(
        json.dumps(content), context["bot_id"], context["conversation_id"]
    )

    def reduce_answer_content(acc, val: Dict):
        if val["type"] == "text":
            return acc + "; " + val["content"]
        else:
            return acc

    def reduce_content(acc, val: List):
        answer_text_content = reduce(reduce_answer_content, val, "")
        if answer_text_content != "":
            return acc + ". " + answer_text_content
        else:
            return acc

    text_content = reduce(reduce_content, bot_answers, "")

    if TEXT_TO_SPEECH_ACTIVATED == True:
        if TEXT_TO_SPEECH_ENGINE == "pyttsx3":
            from server.utils.text_to_speech_pyttsx3 import text_to_speech

            text_to_speech(text_content, guid)
        elif TEXT_TO_SPEECH_ENGINE == "gtts":
            from server.utils.text_to_speech_gtts import text_to_speech

            text_to_speech(text_content, guid)

    return response.json(content)


# TODO: messages sent to client should have a richer format, i.e. not only text should be accepted
# Images, links, videos, text formatting, etc.
# Take into account different possible channels: custom web-chat, WhatsApp, Messenger, Telegram, custom Android chat, etc...
# Different message formatters should be used depending on the channel
# TODO: move message processing logic out of the web server - to the bot engine
def __get_bot_answers_from_rasa_bot_answers(response_text: str):
    rasa_bot_answers = json.loads(response_text)
    if len(rasa_bot_answers) == 0:
        return [[{"type": "text", "content": "Sorry, I have no answer :("}]]

    bot_answers = []
    for rasa_bot_answer in rasa_bot_answers:
        if rasa_bot_answer.get("text") != None:
            bot_answers.append([{"type": "text", "content": rasa_bot_answer["text"]}])
        elif rasa_bot_answer.get("image") != None:
            bot_answers.append([{"type": "image", "content": rasa_bot_answer["image"]}])
        elif rasa_bot_answer.get("custom") != None:
            bot_answers.append(rasa_bot_answer["custom"])

    return bot_answers
