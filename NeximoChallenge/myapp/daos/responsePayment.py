class ResponsePayment():
    def __init__(self,total_amount,total_iva,comission):
        self.amount = total_amount
        self.iva = total_iva
        self.commission = comission

    def add_ammounts(self,responsePaymentToAdd):
        self.amount += responsePaymentToAdd.amount
        self.iva += responsePaymentToAdd.iva
        self.commission += responsePaymentToAdd.commission

    def toDictionary(self):
        return {
            'total':self.amount,
            'taxes':self.iva,
            'commission':self.commission,
        }
    
    def roundSelf(self):
        self.amount = round(self.amount)
        self.iva = round(self.iva)
        self.commission = round(self.commission)
        return self