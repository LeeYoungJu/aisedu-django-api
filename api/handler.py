import json

from django.db.utils import DatabaseError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    handler = exception_handler(exc, context)
    response = {}
    if hasattr(exc, 'default_detail'):
        response['message'] = exc.default_detail
        response['status_code'] = exc.status_code
    elif isinstance(exc, json.decoder.JSONDecodeError):
        response['message'] = 'The request format is invalid'
        response['status_code'] = status.HTTP_400_BAD_REQUEST
    elif isinstance(exc, DatabaseError):
        response['message'] = 'Not found data in database'
        response['status_code'] = status.HTTP_400_BAD_REQUEST
    elif handler:
        response['message'] = handler.status_text
        response['status_code'] = handler.status_code
    else:
        response['message'] = exc.args[0]
        response['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(response['message'], status=response['status_code'], exception=True)
