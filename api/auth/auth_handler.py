from datetime import datetime, timedelta
import jwt
from decouple import config

JWT_SECRET = config()
JWT_ALGORITHM = config()




def access_token(user_id, user_email):
    """
    :param user_id:
    :param user_email:
    :return:
    """
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1, minutes=30),
        'iat': datetime.utcnow(),
        'scope': 'access_token',
        'sub': user_id,
        'cp': user_email
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def token_response(token: str):
    return token

def refresh_token(user_id, user_email):
    """
    :param user_id:
    :param user_email:
    :return:
    """
    payload = {
        'exp': datetime.utcnow() + timedelta(days=0, hours=10),
        'iat': datetime.utcnow(),
        'scope': 'refresh_token',
        'sub': user_id,
        'cp': user_email
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)
