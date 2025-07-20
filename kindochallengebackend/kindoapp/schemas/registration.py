# Schema for creating users
from typing import Optional

from pydantic.v1 import Extra

from kindoapp.models.registration import Registration
from pydantic import BaseModel

class RegistrationCreate(BaseModel):
    firstname :str
    lastname :str
    grade : int
    parent_name:str
    relationship:str
    email: str
    contact :str
    tripdetail_id : int

class RegistrationCreateNoSchool(RegistrationCreate):
    school_id: None = None

class RegistrationResponse(Registration):
    pass
