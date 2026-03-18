from rest_framework import serializers
from .models import Requisicion, DetalleRequisicion, LogRequisicion

#Detalle requiscion
class DetalleRequisicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleRequisicion
        fields = '__all__'

# requisicion
class RequisicionSerializer(serializers.ModelSerializer):
    detalles = DetalleRequisicionSerializer(many=True, required=False)

    class Meta:
        model = Requisicion
        fields = '__all__'


# log_requisicion
class LogRequisicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogRequisicion
        fields = '__all__'
