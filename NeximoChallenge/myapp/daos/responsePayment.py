class ResponsePayment():
    def __init__(self,amount,iva,commission):
        self.amount = amount
        self.iva = iva
        self.commission = commission

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