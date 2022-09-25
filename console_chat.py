from ai_replica.common import get_answer
import json
import requests
from server.utils.read_config import config

SERVER_ADDRESS = config["server"]["address"]
SERVER_PORT = config["server"]["port"]
SERVER_URL = f"http://{SERVER_ADDRESS}:{SERVER_PORT}"

"""A simple console interface for the bot's server. """


def get_answer(user_message: str):
    data = {
        "message": user_message,
    }
    response = requests.post(f"{SERVER_URL}/getResponse", data=json.dumps(data))
    bot_messages = json.loads(response.text)["messages"]
    return bot_messages


if __name__ == "__main__":
    print("Just enter something and press Enter. If you want to exit, press CTRL+C")
    while True:
        user_input = input("Enter something:\n")
        answers = get_answer(user_input) or []
        print("\n" + "*Bot*: ")
        for answer in answers:
            for answer_part in answer:
                if answer_part["type"] == "text":
                    print(answer_part["content"] + "\n")
                else:
                    print(
                        f"Cannot display the answer part of type {answer_part['type']}\n"
                    )
