# import mysql.connector
import sqlite3
from os import mkdir

from data import Piston


def connect_to_sqlite(str_sql, data):
    try:
        conn = sqlite3.connect('Moto_Parts/motoparts.db')
    except sqlite3.OperationalError:
        mkdir('Moto_Parts')
    finally:
        conn = sqlite3.connect('Moto_Parts/motoparts.db')
    # conn = sqlite3.connect('/motoparts.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS PISTONS(
                   brand TEXT,
                   model TEXT,
                   tact TEXT,
                   pistonCode TEXT PRIMARY KEY,
                   diameter DOUBLE,
                   totalHeight DOUBLE,
                   pinDiameter DOUBLE,
                   compressionHeight DOUBLE,
                   oversize TEXT
         )""")
    conn.commit()
    print('table created')

    # cursor.execute('DROP TABLE PISTONS;')
    # print('piston inserted')
    # conn.commit()

    cursor.execute(str_sql, data)
    print('piston inserted')
    conn.commit()

    cursor.execute('SELECT * FROM PISTONS;')
    print(cursor.fetchall())
    conn.close()


class connection:
    def __init__(self):
        try:
            self.db = sqlite3.connect('Moto_Parts/motoparts.db')
        except sqlite3.OperationalError:
            mkdir('Moto_Parts')
        finally:
            self.db = sqlite3.connect('Moto_Parts/motoparts.db')
        # self.db = sqlite3.connect('motoparts.db')
        cursor = self.db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS PISTONS(
                           brand TEXT,
                           model TEXT,
                           tact TEXT,
                           pistonCode TEXT,
                           diameter DOUBLE,
                           totalHeight DOUBLE,
                           pinDiameter DOUBLE,
                           compressionHeight DOUBLE,
                           oversize TEXT,
                           PRIMARY KEY(brand,model,tact)
                 )""")
        self.db.commit()
        print('table created')
    # def __init__(self):
    #     self.db = mysql.connector.connect(
    #         host='127.0.0.1',
    #         user='nikos',
    #         password='pergaminos007!',
    #         port='3306',
    #         database='MotoParts'
    #     )

    def select_query(self, str_sql):
        cursor = self.db.cursor()
        cursor.execute(str_sql)
        result = cursor.fetchall()
        return result

    def insert_query(self, str_sql, data):
        cursor = self.db.cursor()
        cursor.execute(str_sql, data)
        self.db.commit()

    def delete_query(self, str_sql, data):
        cursor = self.db.cursor()
        cursor.execute(str_sql, data)
        self.db.commit()

    def init_table(self):
        cursor = self.db.cursor()
        return cursor

    def update_query(self, str_sql):
        cursor = self.db.cursor()
        print(str_sql)
        cursor.execute(str_sql)
        self.db.commit()


# piston = ('yamaha', 'xt', '4t', 'ybgz', '12.5', '43.1', '12.5',
#           '12.5', 'fag12')
# query = ("insert into pistons(brand, model, tact, pistonCode, diameter, totalHeight, pinDiameter, "
#          "compressionHeight, oversize) values (?, ?, ?, ?, ?, ?, ?, ?, ?)")
# connect_to_sqlite(query, piston)
