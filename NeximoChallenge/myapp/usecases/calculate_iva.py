from rest_framework.response import Response
from rest_framework.exceptions import UnsupportedMediaType

from ..utils.constants import MXN, USD, MXN_IVA, USD_IVA, USD_COMMISSION, USD_TO_MXN
from ..daos.responsePayment import ResponsePayment

class Calculator():

    def CalculateIva(self,payments):
        totals = ResponsePayment(0.0,0.0,0.0)

        for payment in payments:
            if payment.currency == MXN:
                totals.add_ammounts(self.calculateMXN(payment.amount))

            elif payment.currency == USD:
                totals.add_ammounts(self.calculateUSD(payment.amount))

            else:
                raise UnsupportedMediaType('Currency not supported'+payment.currency)
            
        return totals.roundSelf()
            
    def calculateMXN(self,amount):
        itemized_amount = ResponsePayment(0.0,0.0,0.0)

        if amount > 500:
            itemized_amount.amount = amount/(1+MXN_IVA)
            itemized_amount.iva = amount - itemized_amount.amount
        else:
            itemized_amount.amount = amount

        return itemized_amount

    def calculateUSD(self,amount):
        itemized_amount = ResponsePayment(0.0,0.0,0.0)

        if (amount * USD_TO_MXN) > 500:
            itemized_amount.amount = amount/(1+USD_IVA+USD_COMMISSION)
            itemized_amount.iva = itemized_amount.amount * USD_IVA
            itemized_amount.commission = itemized_amount.amount *USD_COMMISSION
        else:
            itemized_amount.amount = amount/(1+USD_COMMISSION)
            itemized_amount.commission = itemized_amount.amount *USD_COMMISSION

        return itemized_amount