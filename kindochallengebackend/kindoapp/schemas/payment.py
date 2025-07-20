from typing import Optional

from pydantic import BaseModel, constr


class PaymentCreate(BaseModel):
    card_number: constr(min_length=16, max_length=16)
    expiry_date: str  # MM/YY
    cvv: constr(min_length=3, max_length=3)
    amount: float
    registration_id: Optional[int] =None
    school_id: Optional[int] =None
    activity_id: Optional[int] =None


class PaymentResponse(BaseModel):
    success: bool
    transaction_id: Optional[str] = None
    error_message: Optional[str] = None

class PaymentLegacyCreate(BaseModel):
    parent_name: str
    student_name: str
    school_id:int
    activity_id:int
    card_number: constr(min_length=16, max_length=16)
    expiry_date: str  # MM/YY
    cvv: constr(min_length=3, max_length=3)
    amount: float