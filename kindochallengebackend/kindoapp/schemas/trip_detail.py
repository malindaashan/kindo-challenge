# Schema for creating users
from typing import Optional

from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import relationship



class School(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    id: int
    school_name: str


class TripDetailCreate(BaseModel):
    id: int
    trip_name: str
    trip_location: str
    grade: int
    date: str
    cost: float


class TripDetailInDBBase(TripDetailCreate):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    school: School

class TripDetailResponse(BaseModel):
    success: bool
    data: list[TripDetailInDBBase]
    errorMessage: Optional[str]  = None



School.trips = relationship("TripDetailInDBBase", back_populates="school")
TripDetailInDBBase.school = relationship("School", back_populates="trips")
