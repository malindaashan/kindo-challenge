# middleware.py
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from .context_store import request_context


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request_context.set(request)
        try:
            response = await call_next(request)
        finally:
            request_context.reset(token)
        return response
