from django.urls import path

from .views import ip_validator

urlpatterns = [
    path('', ip_validator)
]