from sqlalchemy.orm import Session

from kindoapp.models.registration import Registration
from kindoapp.repository.registration_repository import RegistrationRepository
from kindoapp.schemas.registration import RegistrationCreate
from kindoapp.services.payment_service import PaymentService


class RegistrationService:

    def __init__(self, db: Session):
        self.reg_repo = RegistrationRepository(db)

    def save_reg_by_parent_form(self, registration: RegistrationCreate) -> any:
        registration = self.reg_repo.create(registration=registration)
        return registration

    def register_with_payment(self, registration: RegistrationCreate) -> any:
        registration = self.reg_repo.create(registration=registration)
        return registration.id
