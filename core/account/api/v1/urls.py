from django.urls import path
from rest_framework.authtoken import views as rest_views
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('register/', views.RegistrationApiView.as_view(), name='user-registration'),
    # login
    path('token/login/', rest_views.ObtainAuthToken.as_view(), name='user-token-login'),
]
