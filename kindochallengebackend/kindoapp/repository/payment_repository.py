from sqlalchemy.orm import Session

from kindoapp.models.payment import Payment
from kindoapp.schemas.payment import PaymentCreate


class PaymentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, payment: PaymentCreate) -> Payment:
        payment_response = PaymentRepository(**payment.model_dump())
        self.db.add(payment_response)
        self.db.commit()
        self.db.refresh(payment_response)
        return payment_response
