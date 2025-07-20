import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from kindoapp.config.get_db import get_db
from kindoapp.services.trip_details_service import TripDetailService

router = APIRouter()

logger = logging.getLogger(__name__)


def get_trip_detail_service(db: Session = Depends(get_db)) -> TripDetailService:
    return TripDetailService(db)


@router.get("/get-all")
def get_all_trip_details(page: int, limit: int,
                         trip_detail_service: TripDetailService = Depends(get_trip_detail_service)):
    return trip_detail_service.get_trip_deatils(page=page, limit=limit)
