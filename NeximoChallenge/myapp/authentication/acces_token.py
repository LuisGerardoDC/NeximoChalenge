from datetime import datetime, timedelta
from jwt import encode

class AccessToken:
    @classmethod
    def for_user(cls, user):
        # Define la información del payload del token
        payload = {
            'user': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=15)
        }

        # Genera y devuelve el token de acceso
        token = encode(payload, 'secret_key', algorithm='HS256')
        return cls(token)

    def __init__(self, token):
        self.token = token

    def __str__(self):
        return self.token