from rest_framework import serializers
from .models import MachineValue
from django.contrib.auth.models import User

class MachineValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineValue
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']
