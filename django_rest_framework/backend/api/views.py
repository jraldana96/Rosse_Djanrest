import json
from django.http import JsonResponse

# PARA REALIZAR MODEL DATA -> PY DICTONARY
from django.forms.models import model_to_dict

# REST FRAMEWORK
from rest_framework.response import Response
# decorators
from rest_framework.decorators import api_view

# MODELS
from productos.models import Producto
from productos.serializers import ProductoSerializer

def api_echorequest(request,*arg,**kwargs):
    body = request.body #byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dict
    except:
        pass
    print(data)
    # print(data.keys()) to access keys of the dictionary of JSON data
    #return JsonResponse({"message":"Hi there, this is your Django API response"})
    # data['headers'] = request.headers # NOT ABLE TO SERIALIZE
    data['headets'] = dict(request.headers) # DO IT DICTONARY
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET) #FORCE DICTONARY
    print(request.GET) #URL QUERY PARAMS

    return JsonResponse(data)

# JSON RESPONSE RAW PROCESS.
def api_home_rawprocess(request,*arg,**kwargs):
    model_data = Producto.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['nombre'] = model_data.nombre
        data['descripcion'] = model_data.descripcion
        data['precio'] = model_data.precio
    return JsonResponse(data)

# JSON BUILT IN PROCESS. DOING DICTONARY EASILY
def api_home_builtin(request,*arg,**kwargs):
    model_data = Producto.objects.all().order_by('?').first()
    data = {}
    if model_data:
        # data = model_to_dict(model_data) # all
        data = model_to_dict(model_data, fields=['id','nombre'])
    return JsonResponse(data)

## DJANGO REST API VIEW . GET REQUESTS
@api_view(["GET"]) #list of allow http methods
def api_home(request,*arg,**kwargs):
    """
    DRF API VIEW
    """
    instance = Producto.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = ProductoSerializer(instance).data
    
    data=request.data
    return Response(data)

## DJANGO REST API VIEW . POST REQUESTS
@api_view(["POST"]) #list of allow http methods
def api_home(request,*arg,**kwargs):
    """
    DRF API VIEW
    """
    #data=request.data # ECHO BACK
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save() # PARA AGREGAR
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"invalido"}, status=400) # weak version of raise_exception=True


