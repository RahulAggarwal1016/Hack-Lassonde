import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/1"

r = requests.get(url)

json_data = r.json()

print(json_data['title'])
