import requests
api_url = "https://jsonplaceholder.typicode.com/todos/100"
todo = {"userId": 1, "title": "Study chinese", "completed": False}
response = requests.put(api_url, json=todo)
print(response.text)