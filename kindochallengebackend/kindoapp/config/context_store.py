from contextvars import ContextVar
from starlette.requests import Request

request_context: ContextVar[Request] = ContextVar("request_context")


def get_request_id():
    request = request_context.get()
    return getattr(request.state, 'requestid', None)

