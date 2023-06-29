from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..utils.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(token)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)