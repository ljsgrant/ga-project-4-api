from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
import jwt
from rest_framework.exceptions import NotFound

from .serializers.common import UserSerializer
from .serializers.populated import PopulatedUserSerializer

User = get_user_model()


class RegisterView(APIView):
    def post(self, request):
        user_to_register = UserSerializer(data=request.data)
        if user_to_register.is_valid():
            user_to_register.save()
            return Response({'message': 'Successfully registered'}, status=status.HTTP_201_CREATED)
        return Response(user_to_register.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):
    def post(self, request):
        incoming_email = request.data.get('email')
        incoming_password = request.data.get('password')
        try:
            user_to_login = User.objects.get(email=incoming_email)
        except User.DoesNotExist:
            raise PermissionDenied(detail='Username or password is incorrect')
        if not user_to_login.check_password(incoming_password):
            raise PermissionDenied(detail='Username or password is incorrect')

        timestamp = datetime.now() + timedelta(hours=10)

        token = jwt.encode(
            {'sub': user_to_login.id, 'exp': int(
                timestamp.strftime('%s')), 'isAdmin': user_to_login.is_staff},
            settings.SECRET_KEY, algorithm='HS256'
        )

        return Response({'token': token, 'message': f"Hi there {user_to_login.username}!"})


class UserDetailView(APIView):

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(detail=f"Can't find user with key {pk}")

    def get(self, _request, pk):
        user = self.get_user(pk=pk)
        serialized_user = PopulatedUserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
