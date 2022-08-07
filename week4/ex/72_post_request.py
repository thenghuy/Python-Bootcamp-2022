import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId":2, "title": "Buy sushi", "completed": True}
response = requests.post(api_url, json=todo)
print(response.text)