from sqlalchemy.orm import Session

from kindoapp.models.registration import Registration
from kindoapp.repository.registration_repository import RegistrationRepository
from kindoapp.schemas.registration import RegistrationCreate


class RegistrationService:

    def __init__(self, db: Session):
        self.reg_repo = RegistrationRepository(db)

    def save_reg_by_parent_form(self, registration: RegistrationCreate) -> Registration:
        """
          Saves a new registration submitted by a parent form.

          This method delegates the creation of a registration record to the
          registration repository layer and returns the created registration object.

          Args:
              registration (RegistrationCreate): The registration data submitted by the parent form.

          Returns:
              Registration: The created registration object as returned by the repository layer.
          """

        registration = self.reg_repo.create(registration=registration)
        return registration

    def register_with_payment(self, registration: RegistrationCreate) -> int:
        """
               Saves a new registration submitted by a parent form with registration.

               This method delegates the creation of a registration record to the
               registration repository layer and returns the created registration id.

               Args:
                   registration (RegistrationCreate): The registration data submitted by the parent form.

               Returns:
                   int: The created registration id.
               """
        registration = self.reg_repo.create(registration=registration)
        return registration.id
