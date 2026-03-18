from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)

urlpatterns = router.urls
