from fastapi import APIRouter

from kindoapp.api.api_v1.endpoints import tripdetail, form

api_router = APIRouter()
api_router.include_router(tripdetail.router, prefix="/trip-details", tags=["trip deatils"])
api_router.include_router(form.router, prefix="/form", tags=["form"])