import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from kindoapp.config.context_store import get_request_id
from kindoapp.config.get_db import get_db
from kindoapp.schemas.full_registration import FullRegistrationRequest
from kindoapp.schemas.payment import PaymentLegacyCreate
from kindoapp.schemas.registration import RegistrationCreate
from kindoapp.services.payment_service import PaymentService, construct_pay_request
from kindoapp.services.registration_service import RegistrationService

router = APIRouter()

logger = logging.getLogger(__name__)


def get_registration_service(db: Session = Depends(get_db)) -> RegistrationService:
    return RegistrationService(db)

def get_payment_service(db: Session = Depends(get_db)) -> PaymentService:
    return PaymentService(db)


@router.post("/register")
async def save_register_by_parent_form(registration: RegistrationCreate,
                                       registration_service: RegistrationService = Depends(get_registration_service)):
    return registration_service.save_reg_by_parent_form(registration=registration)


@router.post("/register-with-payment")
def register_with_payment(payload: FullRegistrationRequest, registration_service: RegistrationService = Depends(get_registration_service),
                          payment_service: PaymentService = Depends(get_payment_service)):
    """
       Registers a student and processes payment.

       Args:
           payload (FullRegistrationRequest): The full registration and payment data.
           registration_service (RegistrationService): Handles registration logic.
           payment_service (PaymentService): Handles payment processing.

       Returns:
           PaymentResponse: The result of the payment process.

       Raises:
           HTTPException: On validation, registration, or payment failures.
       """
    try:
         reg_id = registration_service.register_with_payment(registration=payload.registration)
         return payment_service.process(construct_pay_request(payload), reg_id, payload.registration.email)
    except ValueError as ve:
        logger.error(f"Validation error: {ve} request_id={get_request_id()}")
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        logger.error(f"Unhandled error during register_with_payment: {e} request_id={get_request_id()}")
        raise HTTPException(status_code=500, detail="Internal server error")

