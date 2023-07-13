from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Registrations

# Serializers define the API representation.


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrations
        fields = '__all__'
