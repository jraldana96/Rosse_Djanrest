# FOR VIEWSETS BUT DOES NT GIVE THE GRANULAR CONTROL OF URL POINTING
from rest_framework.routers import DefaultRouter

from productos.viewsets import ProductoViewSet, ProductoGenericViewSet

router = DefaultRouter()
router.register('productos',ProductoGenericViewSet,#ProductoViewSet,
basename = 'productos')
#print(router.urls)
urlpatterns = router.urls