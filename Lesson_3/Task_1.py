from pymongo import MongoClient as MC

""" Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
записывающую собранные вакансии в созданную БД. """

client = MC('localhost', 27017)
db = client['HH_parsing_db']
collection = db.vacancies_collection


def write_vacancies_in_bd(vacancies_dict):
    for item in vacancies_dict:
        if item.get('salary') is None:
            collection.insert_one(
                {
                    '_id': int(item.get('id')),
                    'name': item.get('name'),
                    'url': item.get('alternate_url'),
                    'employer': item.get('employer').get('name'),
                    'area': item.get('area').get('name'),
                    'salary_min': None,
                    'salary_max': None
                }
            )
        else:
            collection.insert_one(
                {
                    '_id': int(item.get('id')),
                    'name': item.get('name'),
                    'url': item.get('alternate_url'),
                    'employer': item.get('employer').get('name'),
                    'area': item.get('area').get('name'),
                    'salary_min': item.get('salary').get('from'),
                    'salary_max': item.get('salary').get('to')
                }
            )
