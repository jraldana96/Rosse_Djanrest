import requests # Library can be use for HTTP API -> ideal for REST
from getpass import getpass

username = input("Usuario:")
passinput = getpass("Contrasenha:")

auth_endpoint = "http://localhost:8000/api/auth/"
auth_response = requests.post(auth_endpoint, json={'username':username,'password':passinput})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}" # MIGHT BE f"Token {token}" with no overrided auth header keyword
    }
    endpoint = "http://localhost:8000/api/productos/"
    get_response = requests.get(endpoint, headers = headers)
   # print(get_response.json())
    data = get_response.json()
    results = data['results']
    
    # iterate over results if pagination
    #next_url = data['next']
    #if next_url is not None:
    #    get_response = requests.get(next_url, headers=headers)
    #    print(get_response.json())