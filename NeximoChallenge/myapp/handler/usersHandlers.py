from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from myapp.authentication.JWTAuthentication import generate_jwt_token
from myapp.utils.serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = generate_jwt_token(user.id)
            return Response({"token":token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            access_token = generate_jwt_token(user.id)
            token = {'access': str(access_token)}
            return Response(token)
        return Response({'error': 'Credenciales inválidas'}, status=400)