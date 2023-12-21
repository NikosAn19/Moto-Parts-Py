import mysql.connector


class connection:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='127.0.0.1',
            user='nikos',
            password='pergaminos007!',
            port='3306',
            database='MotoParts'
        )

    def select_query(self, str_sql):
        cursor = self.db.cursor()
        cursor.execute(str_sql)
        result = cursor.fetchall()
        return result

    def insert_query(self, str_sql, data):
        cursor = self.db.cursor()
        cursor.execute(str_sql, data)
        self.db.commit()

    def delete_query(self, str_sql):
        cursor = self.db.cursor()
        cursor.execute(str_sql)
        self.db.commit()

    def init_table(self):
        cursor = self.db.cursor()
        return cursor

    def update_query(self, str_sql):
        cursor = self.db.cursor()
        cursor.execute(str_sql)
        self.db.commit()