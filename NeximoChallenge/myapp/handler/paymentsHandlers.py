from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..usecases.calculate_iva import Calculator

class CalculatePayment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        num1 = int(request.data.get('num1'))
        num2 = int(request.data.get('num2'))
        result = num1 + num2
        return Response({'result': result})