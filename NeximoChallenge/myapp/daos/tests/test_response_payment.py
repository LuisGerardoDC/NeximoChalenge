from django.test import TestCase
from ..responsePayment import ResponsePayment

class TestResponsePayment(TestCase):
    def test_add_amount_Success(self):
        print(".test_add_amount_Success")
        # Arrange
        response_payment = ResponsePayment(
            amount=100,
            iva=16,
            commission=0
        )
        response_payment_to_add = ResponsePayment(
            amount=1000,
            iva=160,
            commission=10
        )
        expected_response_payment = ResponsePayment(
            amount=1100,
            iva=176,
            commission=10
        )
        #Act

        response_payment.add_ammounts(responsePaymentToAdd=response_payment_to_add)

        #Assert
        self.assertEqual(expected_response_payment.amount,response_payment.amount)
        self.assertEqual(expected_response_payment.iva,response_payment.iva)
        self.assertEqual(expected_response_payment.commission,response_payment.commission)
    
    def test_to_Dictionary_Success(self):
        print("test_to_Dictionary_Success")
        # Arrange
        response_payment = ResponsePayment(
            amount=99,
            iva=16,
            commission=1
        )
        expected_dicionary = {
            'total':99,
            'taxes':16,
            'commission':1,
        }
        #Act

        received_dictionary = response_payment.toDictionary()

        #Assert
        self.assertEqual(expected_dicionary['total'],received_dictionary['total'])
        self.assertEqual(expected_dicionary['taxes'],received_dictionary['taxes'])
        self.assertEqual(expected_dicionary['commission'],received_dictionary['commission'])
