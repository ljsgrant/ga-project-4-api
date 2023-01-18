from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
import jwt

from .serializers.common import UserSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        user_to_register = UserSerializer(data=request.data)
        if user_to_register.is_valid():
            user_to_register.save()
            return Response({'message': 'Successfully registered'}, status=status.HTTP_201_CREATED )
        return Response(user_to_register.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
