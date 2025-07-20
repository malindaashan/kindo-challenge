from sqlalchemy.orm import Session

from kindoapp.models.trip_detail import TripDetail
from kindoapp.repository.trip_detail_repository import TripDetailRepository
from kindoapp.schemas.trip_detail import TripDetailResponse


class TripDetailService:

    def __init__(self, db: Session):
        self.trip_repo = TripDetailRepository(db)

    def get_trip_deatils(self, page: int = 0, limit: int = 100, active_only: bool = True) -> list[TripDetail]:
        """Get paginated list of users"""
        if limit > 100:  # Business rule: max 100 users per request
            limit = 100

        trip_list = self.trip_repo.get_all(page=page, limit=limit)
        return trip_list
    #  return [UserResponse.model_validate(user) for user in users]
