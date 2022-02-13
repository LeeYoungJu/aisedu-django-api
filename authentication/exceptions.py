from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidRefreshToken(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Refresh token is invalid or expired'


class WrongPasswordToken(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Wrong password'
