import psycopg2
from psycopg2 import Error
import configs.database_parsing as conf


class DataBasePage:

    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(
                user=conf.user,
                password=conf.password,
                host=conf.host,
                database=conf.database
            )
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def executions(self, query):
        print("DataBasePage executions")

        with self.conn.cursor() as cursor:
            cursor.execute(query)
            self.conn.commit()

    def selections(self, query):
        print("DataBasePage selections")

        with self.conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def user_from_group(self, name, group):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM auth_user_groups "
            "WHERE user_id = (SELECT id FROM auth_user WHERE username = '" + name + "') AND "
                                                                                    "group_id = (SELECT id FROM auth_group WHERE name = '" + group + "')"
        )
        records = cursor.fetchall()
        cursor.close()
        if len(records) == 1:
            return True

        return False

    def user_from_db(self, name):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM auth_user WHERE username = '" + name + "'")
        records = cursor.fetchall()
        cursor.close()
        if len(records) == 1:
            return True

        return False

    def add_group(self, name_group):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO auth_group (name) VALUES ('" + name_group + "') ON CONFLICT DO NOTHING")
        self.conn.commit()
        cursor.close()


    def close(self):
        self.conn.close()
