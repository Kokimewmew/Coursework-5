from src.DBManager import DBManager
from src.hh_api_class import HeadHunterParser
from src.saver_class import JSONSaver


def collecting_vacancies(user_input):
    """Функция для сбора вакансии по запросу"""
    parser = HeadHunterParser()

    search_query = user_input
    datas = parser.get_vacancies(search_query)
    return datas


def creating_dictionary_list(other):
    """Функция для создания списка словарей по атрибутам"""
    vacancies_list = []
    for item in other['items']:
        salary_from = item['salary'].get('from') if item['salary'] else None
        salary_to = item['salary'].get('to') if item['salary'] else None
        vacancies_list.append(
            {"id": item['id'], "title": item['name'], "city": item['area']['name'], "salary_from": salary_from, "salary_to": salary_to,
             "link": item['url']})

        # vacancies_list.append(item)

    return vacancies_list


def get_print(input_user):
    db = DBManager("Tashbulatov_A_I", "postgres", "localhost", "1234567890")
    if input_user == "1":
        return db.get_companies_and_vacancies_count()
    elif input_user == "2":
        return db.get_all_vacancies()
    elif input_user == "3":
        return db.get_avg_salary()
    elif input_user == "4":
        return db.get_vacancies_with_higher_salary()
    elif input_user == "5":
        input_keyword = input("Введите ключевое слово названия вакансии или компании\n")
        return db.get_vacancies_with_keyword(input_keyword)
    else:
        return f'Неправильный набор'



def saver_json(other):
    """Функция записи списка экземпляров в JSON"""
    saver = JSONSaver()
    saver.insert(other)
