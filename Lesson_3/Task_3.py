from pymongo import MongoClient as MC
from HH_API_parsing import start
from Task_1 import write_vacancies_in_bd


""" Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта. """

client = MC('localhost', 27017)
db = client['HH_parsing_db']
collection = db.vacancies_collection
id_list = []
required_vacancy = input('Введите искомую вакансию: ')
page_num = 0

""" собираем id вакансий для сравнения из БД """
for db_vacancy in collection.find():  #
    id_list.append(db_vacancy['_id'])

vacancies_dict = start(required_vacancy, page_num)  # новый запрос на API
for vacancy in vacancies_dict: # проверяе нет ли новых вакансий
    if int(vacancy['id']) not in id_list:
        write_vacancies_in_bd(vacancy)  # записываем новую вакансию в БД
        print(f"Появилась новая вакансия ID: {vacancy['id']}")
else:
    print('Новых выкансий не найдено.')
