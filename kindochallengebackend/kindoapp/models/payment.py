

from sqlalchemy import Column, Integer, Float, String, func, DateTime, ForeignKey, Boolean

from kindoapp.config.database import Base


class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Float)
    card_number = Column(String)
    expiry_date = Column(String)
    success = Column(Boolean)
    transaction_id = Column(String)
    created_at = Column(DateTime, nullable=True, default=func.current_timestamp())
    registration_id = Column(Integer, ForeignKey('registration.id'), nullable=False, index=True)
