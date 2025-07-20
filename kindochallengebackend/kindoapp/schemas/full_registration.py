from pydantic import BaseModel

from kindoapp.schemas.payment import PaymentRequest
from kindoapp.schemas.registration import RegistrationCreate
from kindoapp.schemas.trip_detail import School


class FullRegistrationRequest(BaseModel):
    registration: RegistrationCreate
    payment: PaymentRequest
    school: School
