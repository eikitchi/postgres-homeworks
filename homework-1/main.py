"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os


def main():
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='1012') as conn:
        with open(os.path.join(os.getcwd(), 'north_data', 'customers_data.csv'), encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row['customer_id'],
                                                                              row['company_name'],
                                                                              row['contact_name']))

        with open(os.path.join(os.getcwd(), 'north_data', 'employees_data.csv'), encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO employees (first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, "
                        "%s, %s)",
                        (row['first_name'],
                         row['last_name'],
                         row['title'],
                         row['birth_date'],
                         row['notes']))

        with open(os.path.join(os.getcwd(), 'north_data', 'orders_data.csv'), encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO order VALUES (%s, %s, %s, %s, %s)", (row['order_id'],
                                                                                  row['customer_id'],
                                                                                  row['employee_id'],
                                                                                  row['order_date'],
                                                                                  row['ship_city']))

    conn.close()


if __name__ == '__main__':
    main()
