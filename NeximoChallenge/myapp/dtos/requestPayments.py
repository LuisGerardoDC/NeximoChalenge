import json

class RequestPayment:
    def __init__(self,amount= 0,currency= 0):
        self.amount = amount
        self.currency = currency

    def marshall_json(json_data):
        data = json.loads(json_data)
        request_payments = []
        for item in data:
            tempRequestPayment =RequestPayment(
                amount=item['amount'],
                currency=item['currency'],
            )
            request_payments.append(tempRequestPayment)
        return request_payments