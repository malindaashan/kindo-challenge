from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from kindoapp.config.database import Base
from kindoapp.models.school import School


class TripDetail(Base):
    __tablename__ = "tripdetail"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trip_name = Column(String)
    trip_location = Column(String)
    grade = Column(Integer)
    date = Column(String)
    cost = Column(Float)
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
    school = relationship(School)