import requests # Library can be use for HTTP API -> ideal for REST

endpoint = "http://localhost:8000/api/productos/1/update/"

data = {
    "nombre":"UPDATED TITULO",
    "precio":"999.99"

}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
