# Schema for creating users
from pydantic import BaseModel
from sqlalchemy.orm import relationship

from kindoapp.models.school import School
from kindoapp.models.trip_detail import TripDetail


class School(BaseModel):
    id: int
    school_name: str

class TripDetailCreate(BaseModel):
    id: int
    trip_name: str
    trip_location: str
    grade: int
    date: str
    cost: float

class TripDetailResponse(BaseModel):
    id: int
    trip_name: str
    trip_location: str
    grade: int
    date: str
    cost: float
    school: School

    class Config:
        orm_mode = True
        from_attributes = True

School.trips = relationship("TripDetail", back_populates="school")
TripDetail.school = relationship("School", back_populates="trips")