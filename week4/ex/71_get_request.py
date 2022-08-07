import requests
url="https://jsonplaceholder.typicode.com/todos/10"
r=requests.get(url)
print(r.text)

