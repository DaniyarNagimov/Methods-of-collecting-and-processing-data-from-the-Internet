from bs4 import BeautifulSoup as BS
import requests
import json

"""
Необходимо собрать информацию о вакансиях на вводимую должность
(используем input или через аргументы) с сайтов Superjob или HH.
Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
Получившийся список должен содержать в себе минимум:
    Наименование вакансии.
    Предлагаемую зарплату (отдельно минимальную и максимальную).
    Ссылку на саму вакансию.
    Сайт, откуда собрана вакансия.
    ### По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
    Структура должна быть одинаковая для вакансий с обоих сайтов.
    Общий результат можно вывести с помощью dataFrame через pandas.
"""
page = 0
vacancy = input('Введите искомую вакансию: ')


def inquiry_func(vacancy1, page1):
    url = 'https://api.hh.ru/vacancies'
    data = []
    inquiry = requests.get(url, params={'text': f'{vacancy1}', 'area': '1624', 'page': page1, 'per_page': 100})

    with open(f'vacancies_list_{page1}.json', 'w', encoding='utf-8') as js:
        json.dump(inquiry.json(), js)

    with open(f'vacancies_list_{page1}.json', encoding='utf-8') as file:
        qwe = json.load(file)
        for key in qwe:
            data.append(qwe[key])

    return data


""" Парсинг по словарю"""


def parsing_dict(my_dict):
    vacancies_dict = {}
    for i in my_dict:
        if i.get('salary') is None:
            vacancies_dict[i.get('name')] = f"з/п не указана\n" \
                                            f"URL: {i.get('alternate_url')}\n" \
                                            f"Работодатель: {i.get('employer').get('name')}\n" \
                                            f"Расположение: {i.get('area').get('name')}"
        else:
            vacancies_dict[i.get('name')] = f"Зарплата:\n" \
                                            f"    От: {i.get('salary').get('from')}\n" \
                                            f"    До: {i.get('salary').get('to')}\n" \
                                            f"URL: {i.get('alternate_url')}\n" \
                                            f"Работодатель: {i.get('employer').get('name')}\n" \
                                            f"Расположение: {i.get('area').get('name')}"

    return vacancies_dict


""" парсинг через URL вакансии"""


def parsing_url(my_dict):
    vacancies_url = []
    for i in my_dict:
        vacancies_url.append(i.get('alternate_url'))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36', }
    session = requests.session()
    vacancies_dict = {}
    for el in vacancies_url:
        inquiry_to_vacancy_ulr = session.get(el, headers=headers).content.decode('UTF-8')
        soup = BS(inquiry_to_vacancy_ulr, 'lxml')
        vacancy_name = ''
        salary = ''
        for i in soup.find('h1', class_='bloko-header-1'):
            vacancy_name = i.text
        for i in soup.find('p', class_='vacancy-salary'):
            salary = i.text
        vacancies_dict[vacancy_name] = f'{salary}\n' \
                                       f'{el}'

    return vacancies_dict


def print_result(func):
    for el in func:
        print(f'{el}\n{func[el]}\n{"-" * 30}')


while inquiry_func(vacancy, page)[2] > page:
    pages_count = inquiry_func(vacancy, page)[2]
    page = int(input(f'Страниц всего {pages_count}. '
                     f'Введите номер страницы(от 0 до {pages_count}. {pages_count} = Выход): '))
    vacancies_data = inquiry_func(vacancy, page)[0]
    print_result(parsing_dict(vacancies_data))
    # print_result(parsing_url(vacancies_data))
