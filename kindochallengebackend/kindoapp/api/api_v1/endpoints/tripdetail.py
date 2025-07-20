import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from kindoapp.config.context_store import get_request_id
from kindoapp.config.get_db import get_db
from kindoapp.services.trip_details_service import TripDetailService

router = APIRouter()

logger = logging.getLogger(__name__)


def get_trip_detail_service(db: Session = Depends(get_db)) -> TripDetailService:
    return TripDetailService(db)


@router.get("/get-all")
def get_all_trip_details(page: int, limit: int,
                         trip_detail_service: TripDetailService = Depends(get_trip_detail_service)):
    """
        Retrieves a paginated list of trip details.

        Args:
            page (int): The page number to retrieve.
            limit (int): Number of items per page.
            trip_detail_service (TripDetailService): Dependency injection for the trip service.

        Returns:
            List[TripDetail]: A list of trip detail records.

        Raises:
            HTTPException: If service call fails or input is invalid.
        """
    try:
        return trip_detail_service.get_trip_deatils(page=page, limit=limit)
    except ValueError as ve:
        logger.warning(f"Invalid pagination values: {ve} request_id={get_request_id()}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Failed to fetch trip details: {e} request_id={get_request_id()}")
        raise HTTPException(status_code=500, detail="Internal server error")
