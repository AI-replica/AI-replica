from http.server import BaseHTTPRequestHandler
import json

def getUserAndBotInfo(request_handler: BaseHTTPRequestHandler, context):
  result = {
    "user": {
      "id": context["user_id"]
    },
    "bot": {
      "id": context["bot_id"],
      "name": context["bot_name"]
    }
  }

  return {
    "content": json.dumps(result),
    "content_type": "application/json"
  }
