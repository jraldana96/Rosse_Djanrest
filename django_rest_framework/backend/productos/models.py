from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL

# Create your models here.
class ProductoQuerySet(models.QuerySet):
    def es_publico(self):
        return self.filter(publico=True)

    def search(self, query, user=None):
        lookup = Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        qs = self.es_publico().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup) # para incluir las que no pasan es_publico()
            qs = (qs | qs2).distinct() # la union
        return qs

class ProductoManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductoQuerySet(self.model, using = self._db)

    def search(self, query, user=None):
        return self.get_queryset().buscar(query,user)

class Producto(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True,null=True)
    precio = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    publico = models.BooleanField(default = True)

    objects = ProductoManager()

    # PROPERTIES LIKE THIS WONT BE SEND TO JSON model_to_dict RESPONSE ON FIELDS VALUES... WE NEED REST.SERIALIZERS.
    @property
    def precio_liquidacion(self):
        return "%.2f" %(float(self.precio) * 0.5)

    # METHODS
    def dar_descuento(self):
        return "1234"

