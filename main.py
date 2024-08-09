import requests

#Задание 1
params = {'q':'html'}

respond = requests.get('https://api.github.com', params=params)

print("Код статуса: " + str(respond.status_code))
print(respond.json())

#Задание 2
params = {'userId':'1'}

respond = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
print(respond.json())

#Задание 3
params = {'title':'foo', 'body':'bar', 'userId': 1}
respond = requests.post('https://jsonplaceholder.typicode.com/posts', data=params)
print("Код статуса: " + str(respond.status_code))
print(respond.json())