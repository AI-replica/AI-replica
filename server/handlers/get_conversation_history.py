from sanic import Request
import sanic.response as response
import urllib.parse as url_parse
import server.data_access.data_access as data_access


def get_conversation_history(request: Request, context):
    parsed_path = url_parse.urlparse(request.path)
    query = url_parse.parse_qs(parsed_path.query)
    query_top = query.get("$top")
    if query_top != None and len(query_top) > 0:
        top = query_top[0]
    else:
        top = 1000

    messages = data_access.get_conversation_messages(context["conversation_id"], top)

    return response.json(messages)
