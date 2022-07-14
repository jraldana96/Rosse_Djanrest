import requests # Library can be use for HTTP API -> ideal for REST

# similar to the url, might be more than one
endpoint = "https://httpbin.org" 

#get_response = requests.get(endpoint)
#print(get_response.text) # BODY RESPONSE : almost a python dictonary, no able to read null

endpoint = "https://httpbin.org/anything" #will echo back everything
#get_response = requests.get(endpoint)
#print(get_response.json()) # IS a python dictionary, now null is None.

#get_response = requests.get(endpoint, json={"query":"Hello World"} )
#print(get_response.json()) # JSON will apply on data // content type: json app

#get_response = requests.get(endpoint, data={"query":"Hello World"} )
#print(get_response.json()) # data will apply on form // content type: is urlencoded

endpoint = "https://httpbin.org/status/200"
#get_response = requests.get(endpoint)
#print(get_response.status_code) #STATUS CODE 200 

# GET JSON

endpoint = "http://localhost:8000/api/"
#get_response = requests.get(endpoint, params={"abc":123},json={"query":"Hello World"} )
#print(get_response.text)
#print(get_response.status_code)
#print(get_response.json()['message'])
#print(get_response.json())

# POST JSON

#get_response = requests.post(endpoint, json={"producto_id":123} )
#print(get_response.json())

get_response = requests.post(endpoint, json={"nombre":'producto cliente py'} )
print(get_response.json())

# TO LAUNCH ERROR.
#get_response = requests.post(endpoint, json={"abc":'producto cliente py'} )
#print(get_response.json())

get_response = requests.post(endpoint, json={"nombre":'Abc123',"descripcion":"descripcion prueba","precio":99.99} )
print(get_response.json())