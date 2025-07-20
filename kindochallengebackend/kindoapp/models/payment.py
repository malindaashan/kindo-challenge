

from sqlalchemy import Column, Integer, Float, String, func, DateTime, ForeignKey

from kindoapp.config.database import Base


class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Float)
    card_number = Column(String)
    created_at = Column(DateTime, nullable=True, default=func.current_timestamp())
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False, index=True)
    tripdetail_id = Column(Integer, ForeignKey('tripdetail.id'), nullable=False, index=True)
    registration_id = Column(Integer, ForeignKey('registration.id'), nullable=False, index=True)