from rest_framework import generics

from productos.models import Producto
from productos.serializers import ProductoSerializer

class SearchListView(generics.ListAPIView):
    queryset= Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args, **kwargs) # the default
        query = self.request.GET.get('q')
        results = Producto.objects.none()
        if query is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(query=query, user=user)
        return results
