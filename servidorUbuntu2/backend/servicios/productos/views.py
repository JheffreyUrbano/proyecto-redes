from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Proveedor, Producto
from .serializers import ProveedorSerializer, ProductoSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.query_params.get('estado')

        if estado is not None:
            queryset = queryset.filter(estado=estado)

        return queryset


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
