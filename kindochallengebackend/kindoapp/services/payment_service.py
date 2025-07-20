import threading

from sqlalchemy.orm import Session

from kindoapp.repository.payment_repository import PaymentRepository
from kindoapp.schemas.full_registration import FullRegistrationRequest
from kindoapp.schemas.payment import PaymentLegacyCreate, PaymentCreate
from kindoapp.services.email_service import  send_payment_success_email
from kindoapp.services.legacy.payment_processor import LegacyPaymentProcessor, PaymentResponse


def construct_pay_request(full_registration: FullRegistrationRequest) -> PaymentLegacyCreate:
    # Construct the legacy model
    legacy_payment = PaymentLegacyCreate(
        parent_name=full_registration.registration.parent_name,
        school_id=full_registration.school.id,
        activity_id=full_registration.registration.tripdetail_id,
        student_name=full_registration.registration.firstname +" "+ full_registration.registration.lastname,
        card_number=full_registration.payment.card_number,
        expiry_date=full_registration.payment.expiry_date,
        cvv=full_registration.payment.cvv,
        amount=full_registration.payment.amount
    )
    return legacy_payment


def construct_transaction_schema(pay_data: PaymentLegacyCreate, response: PaymentResponse, reg_id: int) -> PaymentCreate:

    transaction = PaymentCreate(
        card_number=pay_data.card_number,
        expiry_date=pay_data.expiry_date,
        amount=pay_data.amount,
        registration_id=reg_id,
        transaction_id=response.transaction_id,
        success=response.success,
    )
    return transaction

class PaymentService:
    def __init__(self, db: Session):
        self.pay_repo = PaymentRepository(db)
        self.processor = LegacyPaymentProcessor()

    def process(self, pay_data: PaymentLegacyCreate, reg_id: int, email: str) -> PaymentResponse:
        response = self.processor.process_payment(pay_data.model_dump())
        if response.success:
            self.pay_repo.create(construct_transaction_schema(pay_data, response, reg_id))

            # Start a new thread for sending the email
            threading.Thread(
                target=send_payment_success_email,
                args=(response.transaction_id, pay_data.amount, email),
                daemon=True
            ).start()


        return PaymentResponse(
            success=response.success,
            transaction_id=response.transaction_id,
            error_message=response.error_message
        )
