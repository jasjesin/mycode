import requests

URL = "http://127.0.0.1:5000"

response = requests.get(URL + "/jas")
print(response.json())
