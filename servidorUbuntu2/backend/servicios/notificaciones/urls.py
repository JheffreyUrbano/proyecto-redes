from django.urls import path
from .views import enviar_email

urlpatterns = [
    path('enviar/', enviar_email),
]
