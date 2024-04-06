from django.urls import path
from .views import app_1

urlpatterns = [
    path('', app_1, name='app_1'),
]
