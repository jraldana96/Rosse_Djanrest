import requests # Library can be use for HTTP API -> ideal for REST

endpoint = "http://localhost:8000/api/productos/1/"

get_response = requests.get(endpoint, json={"nombre":'producto cliente py'} )
print(get_response.json())
