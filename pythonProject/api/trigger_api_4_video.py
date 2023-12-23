import json

import requests

URL = "http://127.0.0.1:5000/"
data = [{"likes": 350, "name": "Get a Job Fast", "views": 1890},
        {"likes": 530, "name": "Avoid layoffs", "views": 1943},
        {"likes": 8910, "name": "Get a stable secure job", "views": 18694},
        {"likes": 1432, "name": "Get a good package", "views": 7326},
        {"likes": 979, "name": "Dont rush", "views": 4824}
        ]
headers = {"Content-Type":"application/json"}

for i in range(len(data)):
    response = requests.put(URL + "video/" + str(i), json.dumps(data[i]), headers=headers)
    print(response.json())

input()
response = requests.delete(URL + "video/0")
print(response)

input()
response = requests.get(URL + "video/2")
print(response.json())
