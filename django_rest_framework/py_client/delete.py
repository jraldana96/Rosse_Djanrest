import requests # Library can be use for HTTP API -> ideal for REST

producto_id = input("What is the product id:")
try:
    producto_id = int(producto_id)
except:
    producto_id = None
    print(f"{producto_id} no valido")

if producto_id:
    endpoint = f"http://localhost:8000/api/productos/{producto_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code,get_response.status_code==204)
