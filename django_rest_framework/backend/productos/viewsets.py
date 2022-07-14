from rest_framework import viewsets, mixins

from .models import Producto
from .serializers import ProductoSerializer

# CAN MANAGE VARIOUS VIEW WITH FEW LINES
class ProductoViewSet(viewsets.ModelViewSet):
    '''
    GET -> LIST -> QUERYSET
    GET -> RETRIEVE -> PRODUCTO INSTANCE DETAIL VIEW
    POST -> CREATE -> NEW INSTANCE
    PUT -> UPDATE
    PATCH -> PARTIAL UPDATE
    DELETE -> DESTROY
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk' #default


# more custom generic viewset
# viewsets can inherited from mixins as in views.py
class ProductoGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    '''
    GET -> LIST -> QUERYSET
    GET -> RETRIEVE -> PRODUCTO INSTANCE DETAIL VIEW
    '''
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk' #default


# BELOW CAN BE USE  in  PRODUCTOS.URLS like alternative to the GenericAPIViews 
producto_lista_viewset = ProductoGenericViewSet.as_view({'get':'list'})
producto_detalle_viewset = ProductoGenericViewSet.as_view({'get':'retrieve'})