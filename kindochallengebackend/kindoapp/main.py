from fastapi import FastAPI

from kindoapp.api.api_v1.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/kindo/api/v1")

@app.get("/servicecheck")
async def service_check():
    return {"message": "This is servicecheck message from kindo app"}