from src.connect_to_postgresql import connection_to_data
from src.utils import collecting_vacancies, creating_dictionary_list, saver_json, get_print

if __name__ == "__main__":
    list_of_company = ["Caltat", "RedLab", "Центр финансовых технологий", "BRANDPOL",
                       "Offer Now", "Безлимит", "Datanomica", "DNS Технологии",
                       "Яндекс", "Тинькофф", "ЧУ ДО Московская школа программистов"]  # Список компании

    vacancies_list = []
    for search_query in list_of_company:  # Цикл по созданию списка словарей, ключом которых является название компании
        coll_vacancies = collecting_vacancies(search_query)
        vacancies_list_item = {search_query: creating_dictionary_list(coll_vacancies)}
        vacancies_list.append(vacancies_list_item)

    saver_json(vacancies_list)  # Сохранение данных в JSON файл

    connection_to_data(vacancies_list)

    while True:
        input_user = input("""
1. Получить список всех компаний и количество вакансий у каждой компании
2. Получить список всех вакансий с указанием названия компании,названия вакансии и зарплаты и ссылки на вакансию.
3. Получить среднюю зарплату по вакансиям
4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.
5. Получить список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
Наберите стоп или stop для выхода из программы
""").lower().strip()
        if get_print(input_user) == "стоп":
            break
