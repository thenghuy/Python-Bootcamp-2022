import requests
api_url = "https://jsonplaceholder.typicode.com/todos/100"
todo = {"userId": 122}
response = requests.patch(api_url, json=todo)
print(response.text)