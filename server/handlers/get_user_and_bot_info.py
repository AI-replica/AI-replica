from sanic import Request
import sanic.response as response


def get_user_and_bot_info(request: Request, context):
    result = {
        "user": {"id": context["user_id"]},
        "bot": {"id": context["bot_id"], "name": context["bot_name"]},
    }

    return response.json(result)
