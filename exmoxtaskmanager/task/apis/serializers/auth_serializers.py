from rest_auth.models import TokenModel
from rest_framework import serializers
from django.contrib.auth.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'username', 'id', 'email']


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """
    user = UserInfoSerializer(many=False, read_only=True)

    class Meta:
        model = TokenModel
        fields = ['key', 'user']
