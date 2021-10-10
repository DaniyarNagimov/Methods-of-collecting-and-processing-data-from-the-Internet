import requests
import json

"""Посмотреть документацию к API GitHub, 
разобраться как вывести список репозиториев для конкретного пользователя,
 сохранить JSON-вывод в файле *.json."""

username = 'TheAlgorithms'

URL = f'https://api.github.com/users/{username}/repos'

inquiry = requests.get(URL)
task_1_result = inquiry.json()

with open('Task_1_result.json', 'w') as js:
    json.dump(task_1_result, js)
