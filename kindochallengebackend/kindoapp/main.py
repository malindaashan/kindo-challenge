import logging
import os
import random
import time

from fastapi import FastAPI, Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from kindoapp.api.api_v1.api import api_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
app = FastAPI()

app.include_router(api_router, prefix="/kindo/api/v1")


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    """
       Middleware that logs incoming HTTP requests and outgoing responses.

       Logs the HTTP method, request URL, and optionally the request body and response status.
       Can be useful for debugging, auditing, and monitoring API behavior.

       Args:
           request (Request): The incoming FastAPI request object.
           call_next (Callable): The next middleware or route handler to call.

       Returns:
           Response: The HTTP response returned by the route handler.

       Raises:
           Exception: Any unhandled exceptions from downstream middleware or route handlers.
       """

    start_time = time.time()
    request_id = ''

    try:
        request_id = generate_unique_request_id(10)
        request.state.requestid = request_id
        request.state.url = str(request.url)

    except Exception as e:
        logger.error(f"logging_middleware error{e}")

    # Log Request
    logger.info(f"action=request_start; method={request.method}; request_id={request_id}; "
                f"url={str(request.url)}; request_params={request.path_params};  "
                f"request.query_params={request.query_params}; user_agent={request.headers.get('user-agent')} ")

    response = await call_next(request)

    # Log response
    process_time = time.time() - start_time
    logger.info(
        f"action=request_complete; method:{request.method};  "
        f"request_id={request_id} url={str(request.url)}; status_code={response.status_code}; "
        f"process_time_ms={round(process_time * 1000, 2)}")
    return response


def generate_unique_request_id(length):
    return int(''.join([str(random.randint(0, 10)) for _ in range(length)]))

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_react():
    index_path = os.path.join("static", "build", "index.html")
    print(index_path)
    with open(index_path) as f:
        html = f.read()
    return HTMLResponse(content=html, status_code=200)

@app.get("/servicecheck")
async def service_check():
    return {"message": "This is servicecheck message from kindo app"}
