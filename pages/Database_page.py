import psycopg2
from psycopg2 import Error
import configs.database_parsing as conf
from configs.common_parsing import new_username


class DataBasePage:

    def __init__(self):
        self.conn = None

    def create_connection(self):
        print("DataBasePage create_connection")

        connect_database = None

        try:
            connect_database = psycopg2.connect(
                user=conf.user,
                password=conf.password,
                host=conf.host,
                database=conf.database
            )
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        return connect_database

    def executions(self, connection, query):
        print("DataBasePage executions")

        self.conn = connection
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            self.conn.commit()

    def selections(self, connection, query):
        print("DataBasePage selections")

        self.conn = connection
        with self.conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def user_info(self, connection, query):
        result = self.selections(connection, query)
        db_first_name = ''
        db_last_name = ''
        db_email = ''
        for el in result:
            db_first_name += el[0]
            db_last_name += el[1]
            db_email += el[2]
        return f'{db_first_name}, {db_last_name}, {db_email}'

    def user_and_group_id(self, conn, us_id, gr_id):
        print("DataBasePage user_and_group_id")

        id_user = self.selections(conn, us_id)
        id_group = self.selections(conn, gr_id)
        return id_user + id_group

    def user_and_group_id_in_group(self, conn, us_id_gr, gr_id_gr):
        print("DataBasePage user_and_group_id_in_group")

        id_user_group = self.selections(conn, us_id_gr)
        id_group_group = self.selections(conn, gr_id_gr)
        return id_user_group + id_group_group

    def check_user_in_group(self, conn, us_id, gr_id, us_id_gr, gr_id_gr):
        print("DataBasePage check_user_in_group")

        user_group_id = self.user_and_group_id(conn, us_id, gr_id)
        user_group_id_in_group = self.user_and_group_id_in_group(
            conn,
            us_id_gr,
            gr_id_gr
        )
        if user_group_id == user_group_id_in_group:
            return f'{new_username} is in the group {conf.group_name}'
        else:
            return f'{user_group_id} is not {user_group_id_in_group}'
