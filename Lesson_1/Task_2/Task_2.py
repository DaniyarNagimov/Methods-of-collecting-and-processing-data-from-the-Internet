import json
import requests





URL = "https://www.mediawiki.org/w/api.php"

PARAMS_0 = {
    'action': "query",
    'meta': "tokens",
    'type': "login",
    'format': "json"
}

R = requests.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

PARAMS_1 = {
    'action': "login",
    'lgname': "Briari111",
    'lgpassword': "R`$:LbUAT<\H[Tyd",
    'lgtoken': LOGIN_TOKEN,
    'format': "json"
}

R = requests.post(URL, data=PARAMS_1)
DATA = R.json()

search_params = {
    'action': 'opensearch',
    'search': 'Python'
}

search_text = requests.get(url=URL, params=search_params)
task_2_result = search_text.json()

with open('Task_2_result.json', 'w') as js:
    json.dump(task_2_result, js)
