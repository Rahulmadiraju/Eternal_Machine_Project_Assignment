from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineValueViewSet, UserViewSet

router = DefaultRouter()
router.register(r'machines', MachineValueViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]
