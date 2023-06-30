from django.test import TestCase
from ..serializers import UserSerializer

class TestSerializers(TestCase):
    def Test_create_success(self):
        print("Test_create_success")
        # Arrange
        serializer = UserSerializer()
        validated_data ={
            'email':"correo@correo.com",
            'password':"GLpop123",
            'first_name':"Luis",
            'last_name':"Hernandez",
        }
        # Act
        response = serializer.create(validated_data)
        #Assert
        self.assertIsNotNone(response)