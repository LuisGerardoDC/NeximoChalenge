import json

class RequestPayment:
    def __init__(self,amout,currency):
        self.amount = amout
        self.currency = currency

    def marshall_json(json_data):
        data = json.loads(json_data)
        request_payments =[]
        for item in data:
            tempRequestPayment =RequestPayment(
                amout=item['amount'],
                currency=item['currency'],
            )
            request_payments.append(tempRequestPayment)
        return request_payments