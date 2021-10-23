from pymongo import MongoClient as MC

"""Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы"""

client = MC('localhost', 27017)
db = client['HH_parsing_db']
collection = db.vacancies_collection
desired_salary = int(input('Введите желаемую з/п: '))

for vacancy in collection.find():
    if vacancy['salary_min'] is not None and int(vacancy['salary_min']) > desired_salary:
        print(f"Вакансия: {vacancy['name']}\n"
              f"Ссылка: {vacancy['url']}\n"
              f"Зарплата:\n"
              f"    MIN: {vacancy['salary_min']}\n"
              f"    MAX: {vacancy['salary_max']}\n"
              f"Работодатель: {vacancy['employer']}\n"
              f"Расположение: {vacancy['area']}\n"
              f"{('-' * 30)}")
