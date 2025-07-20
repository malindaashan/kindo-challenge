from typing import Any, List

from sqlalchemy.orm import Session, joinedload

from sqlalchemy.orm import Session, joinedload

from kindoapp.models.trip_detail import TripDetail
from kindoapp.schemas.trip_detail import TripDetailResponse


class TripDetailRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, page, limit) -> list[type[TripDetail]]:
        """Get all users with pagination"""
        query = self.db.query(TripDetail)

        return query.offset(page).limit(limit).options(joinedload(TripDetail.school)).all()
