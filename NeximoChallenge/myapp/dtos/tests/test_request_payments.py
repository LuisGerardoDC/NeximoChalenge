from django.test import TestCase
from ..requestPayments import RequestPayment

class TestRequestPayment(TestCase):
    def test_marshall_json_success(self):
        print("test_marshall_json_success")
        # Arrange
        json_to_marshall ='[{"amount":1160,"currency":"USD"},{"amount":400,"currency":"MXN"},{"amount":500,"currency":"MXN"}]'
        expected_array_req_pay = [
            RequestPayment(amount=1160,currency="USD"),
            RequestPayment(amount=400,currency="MXN"),
            RequestPayment(amount=500,currency="MXN"),
        ]
        #Act

        marshalled_array_req_payment = RequestPayment.marshall_json(json_to_marshall)

        #Assert
        for i in range(len(expected_array_req_pay)):
            self.assertEqual(expected_array_req_pay[i].amount,  marshalled_array_req_payment[i].amount,    "amout not equal")
            self.assertEqual(expected_array_req_pay[i].currency,marshalled_array_req_payment[i].currency,  "currency not equal")