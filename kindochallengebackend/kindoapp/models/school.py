

from sqlalchemy import Column, Integer, Float, String, func, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from kindoapp.config.database import Base


class School(Base):
    __tablename__ = "school"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    school_name = Column(String)

    trips = relationship("TripDetail", back_populates="school")