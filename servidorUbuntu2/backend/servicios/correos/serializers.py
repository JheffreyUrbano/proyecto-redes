from rest_framework import serializers
from .models import Correo

class CorreoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Correo
        fields = "__all__"
