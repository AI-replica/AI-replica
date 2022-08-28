from http.server import BaseHTTPRequestHandler
import json
import requests
from ai_replica.common import get_answer
from server.constants import CONTENT_TYPES
import server.data_access as data_access
from server.read_config import config
from server.text_to_speech import text_to_speech

BOT_ENGINE = config["bot_engine"]
RASA_REST_WEBHOOK = config["rasa"]["rest_webhook"]
TEXT_TO_SPEECH_ACTIVATED = config["server"]["text_to_speech_activated"]


def getResponse(request_handler: BaseHTTPRequestHandler, context):
    length = int(request_handler.headers.get("content-length"))
    data = request_handler.rfile.read(length)
    obj = json.loads(data)
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
        response = requests.post(url, data=json.dumps(data))
        print(f"rasa resp: {response.text}")
        bot_answers = __get_bot_answers_from_rasa_bot_answers(response.text)
    else:
        bot_answers = [get_answer(user_message)]

    content = json.dumps({"messages": bot_answers})
    data_access.add_message(content, context["bot_id"], context["conversation_id"])

    # TODO: provide text from the bot answers. Currenlty bot answers are tree of content: text, images, ect. Need to extract only text content out of there.
    if TEXT_TO_SPEECH_ACTIVATED == True:
        text_to_speech("Check my answer!")

    return {"content": content, "content_type": CONTENT_TYPES.APPLICATION_JSON}


# TODO: messages sent to client should have a richer format, i.e. not only text should be accepted
# Images, links, videos, text formatting, etc.
# Take into account different possible channels: custom web-chat, WhatsApp, Messenger, Telegram, custom Android chat, etc...
# Different message formatters should be used depending on the channel
# TODO: move message processing logic out of the web server - to the bot engine
def __get_bot_answers_from_rasa_bot_answers(response_text):
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
