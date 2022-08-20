""" RequestHandlers directs incoming requests to appropriate handlers. It is an orhecstrator/controller. """
# TODO: use some Python webserver
from http.server import BaseHTTPRequestHandler
from logging import handlers
import mimetypes
import os.path
import urllib.parse as url_parse
from server.handlers.getConversationHistory import getConversationHistory
from server.handlers.getResponse import getResponse
from server.handlers.getUserAndBotInfo import getUserAndBotInfo
from server.read_config import config

STATIC_FILES_DIR = config["server"]["static_files_dir"]
ANONYMOUS_USER_ID = config["server"]["anonymous_user_id"]


class RequestHandler(BaseHTTPRequestHandler):
    bot_id = "bot"
    user_id = ANONYMOUS_USER_ID
    context = {
        "bot_id": bot_id,
        "bot_name": "Ben",
        "user_id": user_id,
        "conversation_id": f"{bot_id}_{user_id}",
    }
    handlers_get = {
        "/getConversationHistory": getConversationHistory,
        "/getUserAndBotInfo": getUserAndBotInfo,
    }
    handlers_post = {"/getResponse": getResponse}

    def do_GET(self):
        print(f"GET method is called: {self.path}")

        parsed_path = url_parse.urlparse(self.path)
        query = url_parse.parse_qs(parsed_path.query)
        path = parsed_path.path

        if path == "/":
            path = "/index.html"
            if query.get("user"):
                self.user_id = query.get("user")

        last_slash_index = path.rfind("/")
        resource_name = (
            path if last_slash_index == -1 else path[(last_slash_index + 1) :]
        )

        last_dot_index = resource_name.rfind(".")
        resource_extension = ""
        if last_dot_index != -1:
            resource_extension = resource_name[(last_dot_index + 1) :]

        content = None
        content_type = ""
        # if extension is present, serve static files
        if resource_extension != "":
            content = self.__get_static_file_content(path)
            if content != None:
                content_type = mimetypes.guess_type(path)[0]
        # if there is no extension, treat request as api request
        else:
            api_resp = self.__get_api_get_response()
            if api_resp != None:
                content = (api_resp["content"] or "").encode("utf8")
                content_type = api_resp["content_type"]

        if content_type != "":
            self.send_response(200)
        else:
            self.send_response(404)
        self.send_header("Content-type", content_type)
        self.end_headers()

        if content:
            self.wfile.write(content)

    # TODO: A simple router should be implemented to select actions based on request path.
    def do_POST(self):
        print(f"POST method is called: {self.path}")
        parsed_path = url_parse.urlparse(self.path)
        query = url_parse.parse_qs(parsed_path.query)
        path = parsed_path.path
        handler = self.handlers_post.get(path)
        if handler == None:
            self.send_response(404)
            self.end_headers()
            return

        result = handler(self, self.context)
        self.send_response(200)
        self.send_header("Content-type", result["content_type"])
        self.end_headers()
        self.wfile.write(result["content"].encode("utf8"))

    def __get_api_get_response(self):
        parsed_path = url_parse.urlparse(self.path)
        query = url_parse.parse_qs(parsed_path.query)
        path = parsed_path.path
        # TODO: path some general info to the handler, i.e. the context info: local plus request context
        if path == "/getConversationHistory":
            return getConversationHistory(self, self.context)
        if path == "/getUserAndBotInfo":
            # TODO: path some general info to the handler, i.e. the context info: local plus request context
            return getUserAndBotInfo(self, self.context)
        return None

    def __get_static_file_content(self, path):
        content = None
        file_path = f"{STATIC_FILES_DIR}{path}"
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                content = f.read()
        return content
