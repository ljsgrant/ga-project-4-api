from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        incoming_password = data.pop('password')
        incoming_password_confirmation = data.pop('password_confirmation')

        if incoming_password != incoming_password_confirmation:
            raise ValidationError(
                {'password_confirmation': 'password confirmation must be the same as password'})

        try:
            password_validation.validate_password(password=incoming_password)
        except ValidationError as err:
            raise ValidationError({'password': err.messages})

        data['password'] = make_password(incoming_password)

        return data

    class Meta:
        model = User
        fields = '__all__'
