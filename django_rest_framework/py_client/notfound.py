import requests # Library can be use for HTTP API -> ideal for REST

endpoint = "http://localhost:8000/api/productos/15677922324561/"

get_response = requests.get(endpoint)
print(get_response.json())
