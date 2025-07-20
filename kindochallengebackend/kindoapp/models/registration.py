from sqlalchemy import Column, Integer, String, Date, Float, DateTime, func, ForeignKey
from kindoapp.config.database import Base

class Registration(Base):
    __tablename__ = "registration"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    grade = Column(Integer)
    parent_name = Column(Integer)
    relationship = Column(String)
    contact = Column(String)
    email =Column(String)
    created_at = Column(DateTime, nullable=True, default=func.current_timestamp())
    tripdetail_id = Column(Integer, ForeignKey('tripdetail.id'), nullable=False, index=True)