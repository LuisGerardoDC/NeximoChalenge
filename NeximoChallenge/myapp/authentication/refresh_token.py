from datetime import datetime, timedelta
from jwt import encode

class RefreshToken:
    @classmethod
    def for_user(cls, user):
        # Define la información del payload del token
        payload = {
            'user': user.id,
            'exp': datetime.utcnow() + timedelta(days=30)
        }

        # Genera y devuelve el token de actualización
        token = encode(payload, 'secret_key', algorithm='HS256')
        return cls(token)

    def __init__(self, token):
        self.token = token

    def __str__(self):
        return self.token