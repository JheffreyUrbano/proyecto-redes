from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Requisicion, DetalleRequisicion, LogRequisicion
from .serializers import RequisicionSerializer, DetalleRequisicionSerializer, LogRequisicionSerializer

from servicios.correos.services import enviar_correo


class RequisicionViewSet(viewsets.ModelViewSet):
    queryset = Requisicion.objects.all()
    serializer_class = RequisicionSerializer
    lookup_field = 'requino'

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        detalles = data.pop('detalles', [])

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        requisicion = serializer.save()

        # Crear detalles
        for i, det in enumerate(detalles, start=1):
            DetalleRequisicion.objects.create(
                requisicion=requisicion,
                item=i,
                producto_id=det.get('producto'),
                cantidad=det.get('cantidad'),
                valor=det.get('valor', 0)
            )

        # LOG CREACIÓN
        LogRequisicion.objects.create(
            requisicion=requisicion,
            codusuario=requisicion.codusuario,
            accion="CREACION",
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            codestado_anterior=None,
            codestado_nuevo=requisicion.codestado,
            observaciones="Creación de requisición",
            datos_modificados={}
        )

        # CORREO
        enviar_correo(
            destinatario="correo@gmail.com",
            asunto="Nueva requisición creada",
            mensaje=f"Se ha creado la requisición {requisicion.requino}",
            estado="CREADA"
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # LOG CUANDO CAMBIA ESTADO
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        estado_anterior = instance.codestado

        response = super().partial_update(request, *args, **kwargs)

        instance.refresh_from_db()

        LogRequisicion.objects.create(
            requisicion=instance,
            codusuario=instance.codusuario,
            accion="CAMBIO_ESTADO",
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            codestado_anterior=estado_anterior,
            codestado_nuevo=instance.codestado,
            observaciones="Cambio de estado",
            datos_modificados=request.data
        )

        return response


class DetalleRequisicionViewSet(viewsets.ModelViewSet):
    queryset = DetalleRequisicion.objects.all()
    serializer_class = DetalleRequisicionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        requino = self.request.query_params.get('requino')

        if requino:
            queryset = queryset.filter(requisicion__requino=requino)

        return queryset

    @action(detail=False, methods=['delete'], url_path='eliminar')
    def eliminar(self, request):
        item = request.data.get('item')
        codproducto = request.data.get('codproducto')
        requino = request.data.get('requino')

        if not all([item, codproducto, requino]):
            return Response(
                {"error": "Se requieren item, codproducto y requino"},
                status=status.HTTP_400_BAD_REQUEST
            )

        detalle = DetalleRequisicion.objects.filter(
            item=item,
            producto_id=codproducto,
            requisicion_id=requino
        ).first()

        if not detalle:
            return Response({"error": "No encontrado"}, status=404)

        detalle.delete()

        # 🔥 LOG ELIMINACIÓN DETALLE
        LogRequisicion.objects.create(
            requisicion_id=requino,
            codusuario=None,  # puedes mejorarlo luego
            accion="ELIMINACION_DETALLE",
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            codestado_anterior=None,
            codestado_nuevo=None,
            observaciones="Eliminación de detalle",
            datos_modificados=request.data
        )

        return Response({"message": "Eliminado correctamente"}, status=204)

    @action(detail=False, methods=['get'], url_path='eliminar-test')
    def eliminar_test(self, request):
        item = request.query_params.get('item')
        codproducto = request.query_params.get('codproducto')
        requino = request.query_params.get('requino')

        if not all([item, codproducto, requino]):
            return Response(
                {"error": "Faltan parámetros"},
                status=400
            )

        detalle = DetalleRequisicion.objects.filter(
            item=item,
            producto_id=codproducto,
            requisicion_id=requino
        ).first()

        if not detalle:
            return Response({"error": "No encontrado"}, status=404)

        detalle.delete()

        return Response({"message": "Eliminado correctamente"})


class LogRequisicionViewSet(viewsets.ModelViewSet):
    queryset = LogRequisicion.objects.all()
    serializer_class = LogRequisicionSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = super().get_queryset()
        requino = self.request.query_params.get('requino')

        if requino:
            queryset = queryset.filter(requisicion_id=requino)

        return queryset
