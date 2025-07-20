from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from kindoapp.config.database import Base

class TripDetail(Base):
    __tablename__ = "tripdetail"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trip_name = Column(String)
    trip_location = Column(String)
    grade = Column(Integer)
    date = Column(Date)
    cost = Column(Float)
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)

    school = relationship("School", back_populates="trips")