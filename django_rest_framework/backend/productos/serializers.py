from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Producto
from . import validators 

class SecondaryProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'precio',
        ]

class ProductoSerializer(serializers.ModelSerializer):
    #mi_user_data = serializers.SerializerMethodField(read_only=True) # assign THE differentname
    mi_descuento = serializers.SerializerMethodField(read_only=True) # assign THE differentname
    #url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name = 'producto-detalle',
        lookup_field = 'pk'
    ) # Hyperlinked only works on modelSerializer 
    edit_url = serializers.SerializerMethodField(read_only=True)
    # email = serializers.EmailField(write_only=True)
    # with validators
    nombre = serializers.CharField(validators=[validators.validate_nombre_no_hello, validators.unique_nombre_producto])
    # USEGA OF SOURCE
    # titulo = serializers.CharField(source='nombre', read_only=True)
    # email = serializers.EmailField(source='user.email', read_only=True) # if a User is atach to the model
    
    # SERIALIZE SOMETHING ABOUT USER -> FOREIGH KEY
    # user = UserPublicSerializer(read_only=True)
    propietario = UserPublicSerializer(source = 'user',read_only=True)

    class Meta:
        model = Producto
        fields = [
            'user',
            #'mi_user_data',
            'propietario',
            'url',
            'edit_url',
            # 'email',
            'pk',
            'nombre',
            # 'titulo',
            'descripcion',
            'precio',
            'mi_descuento',# a method but differentname -> search for get_differentname
            'precio_liquidacion', # a defined property
        ]

    # raw way to serialize user data
    def get_mi_user_data(self,obj):
        return{
            'username':obj.user.username
        }

    # REPLACED BY HYPERLINKED SHORTCUT
    #def get_url(self, obj):
    #    #return f"/api/productos/{obj.pk}"
    #    request = self.context.get('request') 
    #
    #    if request is None:
    #        return None
    #    return reverse("producto-detalle", kwargs = {'pk': obj.pk}, request=request) # entry view name , kwargs , request

    def get_edit_url(self, obj):
        #return f"/api/productos/{obj.pk}"
        request = self.context.get('request') 

        if request is None:
            return None
        return reverse("producto-editar", kwargs = {'pk': obj.pk}, request=request) # entry view name , kwargs , request


    # IF ITS POSSIBLE TO PROCESS OBJ ATTRIBUTES IT WILL IN CASE IS ONLY DATA IT WONT IF IT IS TRY EXCEPT BLOCK.
    def get_mi_descuento(self, obj):
        # obj is the actual instance of the model i.e: print(obt.id)
        # TRY BLOCK NECCESARY BECAUSE SERIALIZER CLASS ASSUMES THERE IS AN OBJECT ATTACHED, BUT IT MIGHT NOT BECAUSE THE VIEW MIGHT NOT USE serializer.save() AND ONLY CALLS serializer.data
        try:
            return obj.dar_descuento() # method on model
        except:
            return None

        # EXPLICIT ERRORS:
#        if not hasattr(obj, 'id'): # de no tener id es que no existe
#            return None
#        if not isinstance(obj, Producto):
#            return None
#        return obj.dar_descuento()

    # overriding the default method it is not neccesary if all data is validate.
    def create(self, validated_data):
        # return Producto.objects.create(**validated_data)
        # return super().create(validated_data) 
        # email = validated_data.pop('email')
        
        obj = super().create(validated_data)
        # print(email,obj)
        return obj
    
    # if get is called and there is and object already
    def update(self, instance, validated_data):
        #instance.title = validated_data.get('title')
        #return instance # cause is an instance not neccesary save it.
        email = validated_data.pop('email')
        return super().update(instance, validated_data)

    # replaced by validators.py BUT USEFUL FOR REQUEST CONTEXT
    #def validate_nombre(self, value):
#    request = self.request.get('request')
#    user = request. user
#    qs = Producto.objects.filter(user=user, title__iexact=value)
    #    queryset = Producto.objects.filter(nombre__exact=value) # nombre__iexact para ignorar lowers and uppers
    #    if queryset.exists():
    #        raise serializers.ValidationError(f"{value} ya es un producto")
    #    return value