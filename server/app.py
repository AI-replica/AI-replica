import os
from sanic import Request, Sanic
import sanic.response as response
from server import handlers
import server
from server.utils.cors import add_cors_headers
from server.utils.options import setup_options
from server.utils.read_config import config
from server.handlers.get_user_and_bot_info import (
    get_user_and_bot_info as get_user_and_bot_info_handler,
)
from server.handlers.get_conversation_history import (
    get_conversation_history as get_conversation_history_handler,
)
from server.handlers.get_response import get_response as get_response_handler

STATIC_FILES_DIR = config["server"]["static_files_dir"]
ANONYMOUS_USER_ID = config["server"]["anonymous_user_id"]
SERVER_MODE = os.environ.get("SERVER_MODE")
bot_id = "bot"
user_id = ANONYMOUS_USER_ID
context = {
    "bot_id": bot_id,
    "bot_name": "Ben",
    "user_id": user_id,
    "conversation_id": f"{bot_id}_{user_id}",
}
STATIC_FOLDER = os.path.abspath(STATIC_FILES_DIR)
STATIC_FOLDER_CHAT = os.path.abspath(STATIC_FILES_DIR + "/chat")
CHAT_INDEX_FILE_PATH = os.path.abspath(os.path.join(STATIC_FOLDER_CHAT, "index.html"))

app = Sanic("ReplicaWebApp")

if SERVER_MODE == "development":
    # Add OPTIONS handlers to any route that is missing it
    app.register_listener(setup_options, "before_server_start")

    # Fill in CORS headers
    app.register_middleware(add_cors_headers, "response")

app.static("", STATIC_FOLDER)

# handles React routes requests
# i.e. any requests that do not have "." in the path
# it allows loading React app from arbitrrary app route, e.g. /chat/test, where the home root is /chat/.
@app.get(r"/chat/<file:[^\.]*>")
async def chat_index_file_handler(request, file):
    return await response.file(CHAT_INDEX_FILE_PATH)


@app.get("/getConversationHistory")
async def get_conversation_history(request: Request):
    return get_conversation_history_handler(request, context)


@app.post("/getResponse")
async def get_response(request: Request):
    return get_response_handler(request, context)


@app.get("/getUserAndBotInfo")
async def get_user_and_bot_info(request: Request):
    return get_user_and_bot_info_handler(request, context)
