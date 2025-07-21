from sqlalchemy.orm import Session

from kindoapp.models.trip_detail import TripDetail
from kindoapp.repository.trip_detail_repository import TripDetailRepository
from kindoapp.schemas.trip_detail import TripDetailInDBBase


class TripDetailService:

    def __init__(self, db: Session):
        self.trip_repo = TripDetailRepository(db)

    def get_trip_details(self, page, limit) -> list[TripDetailInDBBase]:
        """Get paginated list of users"""
        if limit > 100:  # Business rule: max 100 users per request
            limit = 100

        return self.trip_repo.get_all(page=page, limit=limit)
