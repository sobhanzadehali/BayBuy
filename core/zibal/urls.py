from django.urls import path, include

app_name = 'zibal'

urlpatterns = [
    path('api/v1/', include('zibal.api.v1.urls')),
]
