# backend/user/views.py
import uuid
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password  # Add this import

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            # Hash the password before saving
            serializer.validated_data['password'] = make_password(data['password'])
            user = serializer.save()

            # Convert 'ObjectId' field to string
            serialized_data = UserSerializer(user).data
            your_object_id_field_value = serialized_data.get('id')

            if isinstance(your_object_id_field_value, uuid.UUID):
                serialized_data['id'] = str(your_object_id_field_value)

            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        data = request.data
        try:
            user = User.objects.get(username=data['username'])
            if check_password(data['password'], user.password):
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
