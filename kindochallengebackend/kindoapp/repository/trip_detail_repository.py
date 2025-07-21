from typing import Any, List

from sqlalchemy.orm import Session, joinedload

from sqlalchemy.orm import Session, joinedload

from kindoapp.models.trip_detail import TripDetail
from kindoapp.schemas.trip_detail import TripDetailResponse, TripDetailInDBBase


class TripDetailRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, page, limit) -> list[TripDetailInDBBase]:
        """Get all users with pagination"""
        trips = (
            self.db.query(TripDetail)
            .options(joinedload(TripDetail.school))  # preload school relationship
            .offset((page-1) * limit)
            .limit(limit)
            .all()
        )
        return [TripDetailInDBBase.model_validate(trip) for trip in trips]