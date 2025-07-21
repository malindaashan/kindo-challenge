from unittest.mock import patch

from kindoapp.schemas.payment import PaymentLegacyCreate
from kindoapp.services.legacy.payment_processor import LegacyPaymentProcessor


def set_up_invalid_expiry_data():
    sample_payment = PaymentLegacyCreate(
        student_name="Emily Johnson",
        parent_name="Alice Johnson",
        school_id=1,
        activity_id=2,
        card_number="1234567812345678",
        expiry_date="13/23",
        cvv="321",
        amount=49.99
    )
    return sample_payment


def set_up_legacy_pay_data():
    sample_payment = PaymentLegacyCreate(
        student_name="Emily Johnson",
        parent_name="Alice Johnson",
        school_id=1,
        activity_id=2,
        card_number="1234567812345678",
        expiry_date="08/26",  # Format MM/YY
        cvv="321",
        amount=49.99
    )
    return sample_payment

def test_success_payment():
    """Test that payment is success."""
    with patch('random.random', return_value=0.2):
        processor = LegacyPaymentProcessor()
        response = processor.process_payment(payment_data=set_up_legacy_pay_data().model_dump())

        assert response.success == True

def test_random_payment_failure():
    """Test that random payment failures work as expected."""
    with patch('random.random', return_value=0.05):  # Force random failure
        processor = LegacyPaymentProcessor()
        response = processor.process_payment(payment_data=set_up_legacy_pay_data().model_dump())

        assert response.success == False
        assert response.error_message == "Payment declined by processor. Please try again."


def test_invalid_expiry_card():
    """Test a successful payment with invalid expiry valid data."""
    with patch('random.random', return_value=0.2):
        processor = LegacyPaymentProcessor()
        response = processor.process_payment(payment_data=set_up_invalid_expiry_data().model_dump())

        assert response.success == False
        assert response.error_message == "Invalid expiry date format. Use MM/YY."
