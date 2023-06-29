import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..usecases.calculate_iva import Calculator
from ..dtos.requestPayments import RequestPayment

class CalculatePayment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        calculator = Calculator()

        payments = self.marshall_json(request)
        response =calculator.CalculateIva(payments=payments)

        return Response(response.toDictionary())
    
    
    def marshall_json(self,request):
        json_data = request.body.decode('utf8')
        data = json.loads(json_data)
        request_payments =[]
        for item in data:
            tempRequestPayment =RequestPayment(
                amout=item['amount'],
                currency=item['currency'],
            )
            request_payments.append(tempRequestPayment)
        return request_payments