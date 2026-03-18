from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('servicios.requisiciones.urls')),
    path('api/notificaciones/', include('servicios.notificaciones.urls')),
    path('api/usuarios/', include('servicios.usuarios.urls')),
    path('api/productos/', include('servicios.productos.urls')),
    path('api/correos/', include('servicios.correos.urls')),
]
