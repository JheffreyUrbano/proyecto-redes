from rest_framework.routers import DefaultRouter
from .views import RequisicionViewSet, DetalleRequisicionViewSet, LogRequisicionViewSet

router = DefaultRouter()
router.register(r'requisiciones', RequisicionViewSet)
router.register(r'detalles', DetalleRequisicionViewSet)
router.register(r'logs', LogRequisicionViewSet, basename='logs')

urlpatterns = router.urls
