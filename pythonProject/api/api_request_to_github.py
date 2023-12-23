import json
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_url1 = "https://jsonplaceholder.typicode.com/todos"
api_url2 = "https://jsonplaceholder.typicode.com/todos/201"
#api_url = "https://api.github.com/users/jasjesin"
#api_url = "https://gitlab.com/api/v4/users/nanuchi/projects"
#api_url = "https://jasdil.atlassian.net/wiki/spaces/MYL/overview?homepageId=532709649"
#api_url = "http://prodata.swmed.edu/download/pub/"

get_response = requests.get(api_url)
print(f"\nInitial Data:\nJSON :{get_response.json()}\nStatus Code: {get_response.status_code}\nHeaders:{get_response.headers}")

todo = {'userId': 1, 'title': 'Buy milk', 'completed': False}
post_response = requests.post(api_url1, json=todo)
#headers = {"Content-Type":"application/json"}
#post_response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(f"\nCreate new record:\nJSON : {post_response.json()}\nResponse Code: {post_response.status_code}")

get_response = requests.get(api_url2)
print(f"\nUpdated Data:\nJSON :{get_response.json()}\nStatus Code: {get_response.status_code}")

todo1 = {"title": "Mow lawn"}
patch_response = requests.patch(api_url, json=todo1)
print(f"\nUpdate:\nJSON : {patch_response.json()}\nResponse Code: {patch_response.status_code}")

get_response = requests.get(api_url)
print(f"\nUpdated Data:\nJSON :{get_response.json()}\nStatus Code: {get_response.status_code}")

delete_response = requests.delete(api_url)
print(f"\nDelete:\nJSON : {delete_response.json()}\nResponse Code: {delete_response.status_code}")

get_response = requests.get(api_url)
print(f"\nUpdated Data:\nJSON :{get_response.json()}\nStatus Code: {get_response.status_code}")

#project_list = response.json()
#data = json.loads(project_list)
#print(project_list, sep='\n')
#[print(x) for x in [data]]
#for project in project_list:
#    print(f"\nProject Name: {project['name']} \nProject URL: {project['web_url']}")
