from django.test import TestCase
from ..calculate_iva import Calculator
from ...dtos.requestPayments import RequestPayment
from ...daos.responsePayment import ResponsePayment

class TestCalculateIva(TestCase):
    def setUp(self):
        self.ONE_MXN_PAYMENT ={
            "payments": [ RequestPayment(amount= 1160,currency="MXN"),],
            "expected": ResponsePayment(amount=1000,iva=160,commission=0),
        }
        self.MULTIPLE_MXN_PAYMENT ={
            "payments": [ 
                RequestPayment(amount= 1160,currency="MXN"),
                RequestPayment(amount= 400,currency="MXN"),
            ],
            "expected": ResponsePayment(amount=1400,iva=160,commission=0),
        }
        self.MIX_CURRENCY_PAYMENT ={
            "payments": [ 
                RequestPayment(amount= 60,currency="USD"),
                RequestPayment(amount= 20,currency="USD"),
                RequestPayment(amount= 1160,currency="MXN"),
            ],
            "expected": ResponsePayment(amount=2187.28,iva=297.02,commission=11.38),
        }

    def test_calculate_Iva_One_Mxn_succes(self):
        print("test_calculate_Iva_One_Mxn_succes")
        # Arrange
        calculator = Calculator()
        # Act
        obtined = calculator.CalculateIva(self.ONE_MXN_PAYMENT['payments'])
        #Assert
        self.assertEqual(obtined.amount,    self.ONE_MXN_PAYMENT['expected'].amount)
        self.assertEqual(obtined.iva,       self.ONE_MXN_PAYMENT['expected'].iva)
        self.assertEqual(obtined.commission,self.ONE_MXN_PAYMENT['expected'].commission)

    def test_calculate_Iva_Multipe_Mxn_succes(self):
        print("test_calculate_Iva_Multipe_Mxn_succes")
        # Arrange
        calculator = Calculator()
        # Act
        obtined = calculator.CalculateIva(self.MULTIPLE_MXN_PAYMENT['payments'])
        #Assert
        self.assertEqual(obtined.amount,    self.MULTIPLE_MXN_PAYMENT['expected'].amount)
        self.assertEqual(obtined.iva,       self.MULTIPLE_MXN_PAYMENT['expected'].iva)
        self.assertEqual(obtined.commission,self.MULTIPLE_MXN_PAYMENT['expected'].commission)

#    def test_calculate_Iva_Mix_Currency_succes(self):
#        print("test_calculate_Iva_Mix_Currency_succes")
#        # Arrange
#        calculator = Calculator()
#        # Act
#        obtined = calculator.CalculateIva(self.MIX_CURRENCY_PAYMENT['payments'])
#        #Assert
#        self.assertEqual(obtined.amount,    self.MIX_CURRENCY_PAYMENT['expected'].amount)
#        self.assertEqual(obtined.iva,       self.MIX_CURRENCY_PAYMENT['expected'].iva)
#        self.assertEqual(obtined.commission,self.MIX_CURRENCY_PAYMENT['expected'].commission)
