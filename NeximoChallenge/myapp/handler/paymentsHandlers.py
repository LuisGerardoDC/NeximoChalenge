from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from myapp.usecases.calculate_iva import Calculator
from myapp.dtos.requestPayments import RequestPayment

class CalculatePayment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        calculator = Calculator()
        json_data = request.body.decode('utf8')
        payments = RequestPayment.marshall_json(json_data)

        response =calculator.CalculateIva(payments=payments)

        return Response(response.toDictionary())
    