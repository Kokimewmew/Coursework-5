import psycopg2


def connection_to_data(vacancies_list):
    conn = psycopg2.connect(
        host="localhost",
        database="Tashbulatov_A_I",
        user="postgres",
        password="1234567890"
    )

    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS company")
    cur.execute("CREATE TABLE company("
                " company_name varchar(100),"
                " title varchar(100),"
                " city varchar(50),"
                " salary_from int,"
                " salary_to int,"
                " link varchar(100))")

    conn.commit()
    for company_dict in vacancies_list:
        company_name = list(company_dict.keys())[0]
        vacancies = company_dict[company_name]
        for vacancy in vacancies:
            title = vacancy['title']
            city = vacancy['city']
            salary_from = vacancy['salary_from']
            salary_to = vacancy['salary_to']
            link = vacancy['link']
            cur.execute(
                "INSERT INTO company (company_name, title, city, salary_from, salary_to, link)"
                " VALUES (%s, %s, %s, %s, %s, %s) returning *",
                (company_name, title, city, salary_from, salary_to, link))

    conn.commit()

    cur.close()
    conn.close()
