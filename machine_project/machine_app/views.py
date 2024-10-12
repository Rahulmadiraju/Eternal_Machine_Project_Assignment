from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import MachineValue
from .serializers import MachineValueSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect  # Import redirect

# Redirect view for the root URL
def redirect_to_admin(request):
    return redirect('/admin/')  # Redirect to the admin interface

# CRUD for MachineValue
class MachineValueViewSet(viewsets.ModelViewSet):
    queryset = MachineValue.objects.all()
    serializer_class = MachineValueSerializer

# User management views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
