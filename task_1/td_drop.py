import psycopg2

db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "mysecretpassword",
    "host": "localhost"
}

drop_tables_commands = [
    """
    DROP TABLE users, status, tasks 
    """
]


def drop_tables():
    conn = None
    try:

        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        for command in drop_tables_commands:
            cur.execute(command)

        conn.commit()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    drop_tables()
