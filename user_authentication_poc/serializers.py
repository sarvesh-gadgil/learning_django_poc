from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializersAuth(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def save(self, **kwargs):
        print(kwargs)

