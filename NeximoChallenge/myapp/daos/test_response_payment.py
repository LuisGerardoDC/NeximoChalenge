from django.test import TestCase
from .responsePayment import ResponsePayment

class TestResponsePayment(TestCase):
    def test_add_amounts(selft):
        # Arrange
        response_payment = ResponsePayment(
            total_amount=100,
            total_iva=16,
            comission=0
        )
        response_payment_to_add = ResponsePayment(
            total_amount=1000,
            total_iva=160,
            comission=10
        )
        expected_response_payment = ResponsePayment(
            total_amount=1100,
            total_iva=176,
            comission=10
        )
        #Act

        response_payment.add_ammounts(responsePaymentToAdd=response_payment_to_add)

        #Assert
        selft.assertEqual(response_payment,expected_response_payment)

