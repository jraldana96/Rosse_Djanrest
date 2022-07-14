from rest_framework import serializers

# para serializar los productos que pertecen a un usuario dado.
class UserProductInlineSerializer(serializers.Serializer):
    url_detalle = serializers.HyperlinkedIdentityField(
        view_name = 'producto-detalle',
        lookup_field = 'pk',
        read_only = True
    )
    nombre = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    
    # FOR NESTED SERIALIZATION
    #other_products = serializers.SerializerMethodField(read_only=True)

    #def get_other_products(self,obj):
    #    #print(obj) # WILL RESULT IN AN USER EVEN THO I HAVENT IMPORT USER MODELS.
    #    user = obj
    #    user_products = user.producto_set.all()[:5]
    #    return UserProductInlineSerializer(user_products, many=True, context = self.context).data