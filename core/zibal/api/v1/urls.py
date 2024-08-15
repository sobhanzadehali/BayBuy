from django.urls import path
from . import views

app_name = 'api-v1'

urlpatterns = [
    path('request/<int:order_id>/', views.send_pay_request, name='send_pay'),
    path('callback', views.callback_view, name='callback'),
]
