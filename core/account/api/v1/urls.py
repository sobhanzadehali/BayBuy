from django.urls import path
from . import views

app_name = 'api-v1'

urlpatterns = [
    # registration
    path('register/', views.RegistrationApiView.as_view(), name='user-registration'),
]
