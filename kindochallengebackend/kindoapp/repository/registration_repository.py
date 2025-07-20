from sqlalchemy.orm import Session

from kindoapp.models.registration import Registration
from kindoapp.models.trip_detail import TripDetail
from kindoapp.schemas.registration import RegistrationCreate


class RegistrationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, registration: RegistrationCreate) -> Registration:
        registration = Registration(**registration.model_dump())
        self.db.add(registration)
        self.db.commit()
        self.db.refresh(registration)
        return registration
