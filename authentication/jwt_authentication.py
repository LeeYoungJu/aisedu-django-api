import json

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.utils import datetime_from_epoch
from rest_framework_simplejwt.settings import api_settings

from .exceptions import InvalidRefreshToken
from config.settings import REFRESH_TOKEN_UPDATE


class CustomJWTAuthentication(JWTAuthentication):

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        new_token = None
        if raw_token is None:
            return None
        elif 'refresh' in raw_token:
            new_token = self.refresh_token(raw_token['refresh'])
            raw_token = new_token

        validated_token = self.get_validated_token(raw_token['access'])
        return self.get_user(validated_token), new_token

    def get_raw_token(self, header):
        """
        Extracts an unvalidated JSON web token from the given "Authorization"
        header value.
        """
        if len(header) == 0:
            # Empty AUTHORIZATION header sent
            return None

        if type(header) is not dict:
            header = json.loads(header)

        return header

    def refresh_token(self, refresh):
        try:
            refresh = RefreshToken(refresh)
            new_refresh = self.get_new_refresh_token(refresh)
        except Exception:
            raise InvalidRefreshToken()

        data = {
            'access': str(refresh.access_token)
        }

        if new_refresh:
            data['refresh'] = new_refresh

        return data

    def get_new_refresh_token(self, refresh):
        claim_time = datetime_from_epoch(refresh.payload['exp'])
        if claim_time - refresh.current_time <= REFRESH_TOKEN_UPDATE:
            refresh.blacklist()
            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            return str(refresh)
        else:
            return None
