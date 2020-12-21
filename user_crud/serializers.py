from rest_framework import serializers
from user_crud.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'is_new', 'contact_no']
