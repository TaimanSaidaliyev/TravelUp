from django.shortcuts import render
from rest_framework.views import Response, APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class GetToken(APIView):
    def post(self, request):
        token = request.data['api_token']
        user_id = Token.objects.get(key=token).user_id
        user = User.objects.get(pk=user_id)
        return Response({
            'id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'email_verified_at': '2023-01-25T12:13:02.000000Z',
            'created_at': user.date_joined,
            'updated_at': user.last_login,
            'api_token': token
            }
        )