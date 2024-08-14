from django.urls import path, include

app_name = 'zibalpay'

urlpatterns = [
    path('api/v1/', include('zibalpay.api.v1.urls')),
]
