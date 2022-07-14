from rest_framework import authentication, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.http import Http404
from django.shortcuts import get_object_or_404

#overrided keyword auth
from api.authentication import TokenAuthentication


from .models import Producto

from api.mixins import (
    StaffEditorPermissionMixin, 
    UserQuerySetMixin)
from api.permissions import IsStaffEditorPermission
from .serializers import ProductoSerializer

# USING GENERICS -> WILL IMPLY THE METHOD
class ProductoListaNuevoAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    # user_field = 'owner' # for override on UserQuerySetMixin

    # BELOW ABOUT AUTH NOT NEEDED IF THERE IS DEFAULT IN REST IN SETTINGS.PY
    #authentication_classes = [
    #    authentication.SessionAuthentication,
    #    TokenAuthentication #authentication.TokenAuthentication
    #    ]    
    
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #permission_classes = [permissions.DjangoModelPermissions] # WILL APPLY ON GET, POST, DELETE, PATCH METHODS ON SINGLE VIEWS.
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # WILL APPLY ON GET, POST, DELETE, PATCH METHODS ON SINGLE VIEWS.\ # NOT NEEDED BECAUSE IS ENHERITARED.

    # YOU MIGHT WANT TO OVERRIDE PERMISSIONS. i.e: permission_classes = [] will cut off all previous permissions.


    # WILL APPLY ON CREATEAPIVIEW
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        #email = serializer.validated_data.pop('email')
        nombre = serializer.validated_data.get('nombre')
        descripcion = serializer.validated_data.get('descripcion') or None
        if descripcion is None:
            descripcion = nombre
        serializer.save(user = self.request.user, descripcion=descripcion)
        # might be added or django signal for example
    

    #def get_queryset(self, *args, **kwargs):
    #    # in views definitivamente habra request opuesto a como se trata en serializers.
    #    qs = super().get_queryset(*args, **kwargs)
    #    request = self.request
    #    user = request.user
    #    if not user.is_authenticated: # wont happen cause Class inherited permissions
    #        return Producto.objects.none()
    #    # print(request.user)
    #    return qs.filter(user = request.user)

# RESULT:
vista_lista_nuevo_producto = ProductoListaNuevoAPIView.as_view()


class ProductoNuevoAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.CreateAPIView):
    """
    NOT WILL USE THIS CAUSE ListCreateAPIView
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # WILL APPLY ON CREATEAPIVIEW
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        nombre = serializer.validated_data.get('nombre')
        descripcion = serializer.validated_data.get('descripcion') or None
        if descripcion is None:
            descripcion = nombre
        serializer.save(descripcion=descripcion)
        # might be added or django signal for example

# RESULT:
vista_nuevo_producto = ProductoNuevoAPIView.as_view()

class ProductoDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,    
    generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # detail view will display one single item
    # lookup_field = 'pk'
# RESULT:
vista_detalle_producto = ProductoDetailAPIView.as_view()

class ProductoUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,    
    generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.descripcion:
            instance.descripcion = instance.nombre

# RESULT:
vista_actualizar_producto = ProductoUpdateAPIView.as_view()



class ProductoDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

# RESULT:
vista_eliminar_producto = ProductoDestroyAPIView.as_view()


class ProductoListaAPIView(
    StaffEditorPermissionMixin,
    generics.ListAPIView):
    """
    NOT WILL USE THIS CAUSE ListCreateAPIView
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # detail view will display one single item
    # lookup_field = 'pk'
# RESULT:
vista_lista_producto = ProductoListaAPIView.as_view()


# MIXING VIEW
# on class based views we define methods for get as opposed to function based views where we define conditionals for get or post
class ProductoMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    lookup_field = 'pk'
    def get(self,request,*args,**kwargs):
        pk = kwargs.get("pk")# REPLACE ARGUMENT ON FUNCTION GET
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # THIS METHODS WILL BE AVAILABLE ON MIXIN EXTENDING GENERICS API
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        nombre = serializer.validated_data.get('nombre')
        descripcion = serializer.validated_data.get('descripcion') or None
        if descripcion is None:
            descripcion = nombre
        serializer.save(descripcion=descripcion)

vista_mixin_producto = ProductoMixinView.as_view()

# USING FUNCTIONAL -> WAY TO ENRICH SERIALIZER
@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            # detail view
            #queryset = Producto.objects.filter(pk=pk)
            #if not queryset.exist():
            #    # raise Http404 # using django
            
            obj = get_object_or_404(Producto, pk=pk)
            data = ProductoSerializer(obj, many=False).data           
            return Response(data)
        else:
            # list view
            queryset = Producto.objects.all()
            data = ProductoSerializer(queryset, many= True).data
            return Response(data)
        
        pass
    elif method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
         
            nombre = serializer.validated_data.get('nombre')
            descripcion = serializer.validated_data.get('descripcion') or None
            if descripcion is None:
                descripcion = nombre
            instance = serializer.save(descripcion=descripcion)
            return Response(serializer.data)
        return Response({"invalid":"invalido"}, status=400) # weak version of raise_exception=True


