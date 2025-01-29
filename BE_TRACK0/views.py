from rest_framework import generics
from rest_framework.response import Response
from django.utils.timezone  import now
from drf_spectacular.utils import extend_schema

class InfoAPIView(generics.GenericAPIView):
    @extend_schema(summary='GET API INFO', description='Returns basic information about the API')
    def get(self, request, *args, **kwargs):
        data = {
            'email': 'ugochukwub79@gmail.com',
             'current_datetime': now().isoformat(timespec='seconds').replace('+00:00', 'Z'),
            'github_url': 'https://github.com/Benji918/HNG-12-BE-TRACK-S0'
        }

        return Response(data, status=200)

