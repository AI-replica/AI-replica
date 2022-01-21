from http.server import BaseHTTPRequestHandler
import json
import mimetypes
import os.path

from ai_replica.common import get_answer

STATIC_FILES_DIR = "./web_chat"

class RequestHandler(BaseHTTPRequestHandler):
  def get_api_get_response(self):
    return json.dumps({"message": "Hello, World! I am Bot!"})

  # Currently, get_answer is the default processed action.
  # Other actions can be added later.
  # TODO: Basically a simple router should be implemented to select actions based on request path.
  def get_api_post_response(self):
    length = int(self.headers.get('content-length'))
    data = self.rfile.read(length)
    obj = json.loads(data)
    user_message = obj["message"]
    bot_answer = get_answer(user_message)

    return json.dumps({"message": bot_answer})

  def do_GET(self):
    print(f"GET method is called: {self.path}")

    path = self.path
    if (path == "/"):
      path = "/index.html"

    last_slash_index = path.rfind("/")
    resource_name = path if last_slash_index == -1 else path[(last_slash_index + 1):]

    last_dot_index = resource_name.rfind(".")
    resource_extension = ""
    if (last_dot_index != -1):
      resource_extension = resource_name[(last_dot_index + 1):]

    content = ""
    content_type = ""
    if (resource_extension != ""):
      file_path = f"{STATIC_FILES_DIR}{path}"
      if (os.path.exists(file_path)):
        with open(file_path) as f:
          content = f.read()
          content_type = mimetypes.guess_type(path)
    else:
      content = self.get_api_get_response()
      content_type = "application/json"

    if (content_type != ""):
      self.send_response(200)
    else:
      self.send_response(404)
    self.send_header("Content-type", content_type)
    self.end_headers()
    
    # For some reason, writing into response wstream should happen after send_response method is called.
    # Otherwise, the content is not sent to the client.
    # TODO: check why it is so.
    self.wfile.write(content.encode("utf8"))

  def do_POST(self):
    print(f"POST method is called: {self.path}")
    content_type = "application/json"
    content = self.get_api_post_response()

    self.send_response(200)
    self.send_header("Content-type", content_type)
    self.end_headers()

    self.wfile.write(content.encode("utf8"))
    