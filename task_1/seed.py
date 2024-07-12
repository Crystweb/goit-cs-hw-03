from faker import Faker
import psycopg2
import random

fake = Faker()
db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "mysecretpassword",
    "host": "localhost"
}


def generate_users(n=100):
    """ Генерує випадкові дані для таблиці користувачів """
    users = [(fake.name(), fake.unique.email()) for _ in range(n)]
    return users


def generate_statuses():
    """ Генерує фіксовані статуси для таблиці статусів """
    statuses = [('new',), ('assigned',), ('in progress',), ('in review',), ('completed',)]
    return statuses


def generate_tasks(n=250):
    """ Генерує випадкові дані для таблиці завдань """
    tasks = []
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = random.randint(1, 5)
        user_id = random.randint(1, 100)
        tasks.append((title, description, status_id, user_id))
    return tasks


def populate_database():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        users = generate_users()
        cur.executemany("INSERT INTO users (name, email) VALUES (%s, %s)", users)

        statuses = generate_statuses()
        cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)

        tasks = generate_tasks()
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    populate_database()
