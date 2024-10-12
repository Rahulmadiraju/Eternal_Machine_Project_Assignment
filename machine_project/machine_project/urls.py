"""
URL configuration for machine_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from machine_app.views import redirect_to_admin  # Import the redirect view

urlpatterns = [
    path('', redirect_to_admin, name='redirect_to_admin'),  # Redirect root URL to admin
    path('admin/', admin.site.urls),  # Django admin site
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token generation
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh
    path('api/', include('machine_app.urls')),  # Include your app's URLs for machine data and user management
]
