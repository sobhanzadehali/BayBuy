from django.urls import path
from rest_framework.authtoken import views as rest_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('register/', views.RegistrationApiView.as_view(), name='user-registration'),
    # login
    path('token/login/', rest_views.ObtainAuthToken.as_view(), name='user-token-login'),
    # logout
    path('token/logout/', views.TokenLogoutView.as_view(), name='user-token-logout'),
    # JWT
    path('jwt/token/', TokenObtainPairView.as_view(), name='jwt-obtain-pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='jwt-token-refresh'),
]
