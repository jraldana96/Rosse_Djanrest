import requests # Library can be use for HTTP API -> ideal for REST

endpoint = "http://localhost:8000/api/productos/"
data = {
    "nombre" : "articulo prueba 2"
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
