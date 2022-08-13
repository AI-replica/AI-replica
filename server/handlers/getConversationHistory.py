from http.server import BaseHTTPRequestHandler
import json
import urllib.parse as url_parse
from server.constants import CONTENT_TYPES
import server.data_access as data_access

def getConversationHistory(request_handler: BaseHTTPRequestHandler, context):
  parsed_path = url_parse.urlparse(request_handler.path)
  query = url_parse.parse_qs(parsed_path.query)
  query_top = query.get("$top")
  if query_top != None and len(query_top) > 0:
    top = query_top[0]
  else:
    top = 1000

  messages = data_access.get_conversation_messages(context["conversation_id"], top)

  return {
    "content": json.dumps(messages),
    "content_type": CONTENT_TYPES.APPLICATION_JSON
  }
