import unittest

from kindoapp.services.payment_service import PaymentService


class TestProcessPayment(unittest.TestCase):
    def setUp(self):
        self.processor = PaymentService()
        self.valid_data = {
            'student_name': 'Ashan Malinda',
            'parent_name': 'Jane',
            'amount': 100.0,
            'card_number': '1234567812345678',
            'expiry_date': '12/25',
            'cvv': '123',
            'school_id': 1,
            'activity_id': 2
        }

    def test_invalid_card_number(self):
        data = self.valid_data.copy()
        data['card_number'] = '12345678'
        response = self.processor.process_payment(data)
        self.assertFalse(response.success)
        self.assertEqual(response.error_message, "Invalid card number. Must be 16 digits.")