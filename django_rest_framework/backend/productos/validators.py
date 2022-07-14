from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Producto

#def validate_nombre(value):
#    queryset = Producto.objects.filter(nombre__exact=value) # nombre__iexact para ignorar lowers and uppers
#    if queryset.exists():
#        raise serializers.ValidationError(f"{value} ya es un producto")
#    return value

def validate_nombre_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"{value} no es valido")
    return value

unique_nombre_producto = UniqueValidator(queryset = Producto.objects.all(), lookup='iexact')