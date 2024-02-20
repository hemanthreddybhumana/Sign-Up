# user/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'username', 'agree_to_terms']

    # Explicitly define the 'id' field as CharField without source
    id = serializers.CharField(read_only=True)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
