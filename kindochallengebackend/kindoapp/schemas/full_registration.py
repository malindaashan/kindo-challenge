from pydantic import BaseModel

from kindoapp.schemas.payment import PaymentCreate
from kindoapp.schemas.registration import RegistrationCreate
from kindoapp.schemas.trip_detail import School


class FullRegistrationRequest(BaseModel):
    registration: RegistrationCreate
    payment: PaymentCreate
    school: School