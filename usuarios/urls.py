from django.urls import path, include
from .views import register 

#me trae las url de accounts sin necesitas usar accounts en la url
app_name = "accounts"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registrar/', register, name='registrar'),
]
