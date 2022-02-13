from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response: Response = renderer_context['response']
        formed_data = {}
        if response.exception:
            formed_data['message'] = data
        else:
            authentication = renderer_context['request'].auth
            if authentication:
                formed_data['token'] = {}
                for token, value in authentication.items():
                    formed_data['token'][token] = value
            formed_data['data'] = data

        return super().render(formed_data, accepted_media_type=accepted_media_type, renderer_context=renderer_context)