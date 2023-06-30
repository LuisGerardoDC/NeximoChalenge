from django.test import TestCase
from ..responsePayment import ResponsePayment

class TestResponsePayment(TestCase):
    def test_add_amount_Success(self):
        print(".test_add_amount_Success")
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
        self.assertEqual(expected_response_payment.amount,response_payment.amount)
        self.assertEqual(expected_response_payment.iva,response_payment.iva)
        self.assertEqual(expected_response_payment.commission,response_payment.commission)
    
    def test_to_Dictionary_Success(self):
        print("test_to_Dictionary_Success")
        # Arrange
        response_payment = ResponsePayment(
            total_amount=99,
            total_iva=16,
            comission=1
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
