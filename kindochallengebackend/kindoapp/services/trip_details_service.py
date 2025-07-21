from sqlalchemy.orm import Session

from kindoapp.models.trip_detail import TripDetail
from kindoapp.repository.trip_detail_repository import TripDetailRepository
from kindoapp.schemas.trip_detail import TripDetailResponse


class TripDetailService:

    def __init__(self, db: Session):
        self.trip_repo = TripDetailRepository(db)

    def get_trip_details(self, page, limit) -> list[TripDetail]:
        """Get paginated list of users"""
        if limit > 100:  # Business rule: max 100 users per request
            limit = 100

        trip_list = self.trip_repo.get_all(page=page, limit=limit)
        return trip_list
