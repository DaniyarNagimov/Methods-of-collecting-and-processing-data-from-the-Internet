import requests
import json


def inquiry_func(vacancy, page):
    url = 'https://api.hh.ru/vacancies'
    inquiry = requests.get(url, params={'text': vacancy, 'area': '1624', 'page': page, 'per_page': 100})
    return inquiry


def write_json(response):
    with open(f'vacancies_list.json', 'w', encoding='utf-8') as js:
        json.dump(response.json(), js)


def load_json():
    with open(f'vacancies_list.json', encoding='utf-8') as file:
        item = json.load(file)
    return item


def start(required_vacancy, page):
    data = []
    item_num = 0
    write_json(inquiry_func(required_vacancy, page))
    item = load_json()
    while item['pages'] > page:
        write_json(inquiry_func(required_vacancy, page))
        item2 = load_json()
        for i in item2['items']:
            data.append(i)
            item_num += 1
        page += 1

    return data
