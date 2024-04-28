class DBManager:
    pass
    """класс DBManager для работы с данными в БД."""

    def get_companies_and_vacancies_count(self):
        #for vacancy_item in vacancies_list:
        #    search_query = list(vacancy_item.keys())[0]
        #    vacancies = vacancy_item[search_query]
        #    print(f"Number of vacancies for {search_query}: {len(vacancies)}")

        """получает список всех компаний и количество вакансий у каждой компании."""


    def get_all_vacancies(self):

        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""

    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""