from six import text_type

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework import serializers

from .models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        refresh = super().get_token(user)
        access_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
        refresh_lifetime = api_settings.REFRESH_TOKEN_LIFETIME
        data = {}
        refresh.set_exp(lifetime=refresh_lifetime)
        access = refresh.access_token
        access.set_exp(lifetime=access_lifetime)
        data['refresh'] = text_type(refresh)
        data['access'] = text_type(access)
        return data

    def validate(self, attrs):
        data = super(TokenObtainPairSerializer, self).validate(attrs)
        return self.get_token(self.user)
