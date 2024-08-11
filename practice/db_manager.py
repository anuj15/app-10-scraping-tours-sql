import sqlite3


class DBManager:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(database=db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str):
        query = f'create table if not exists {table_name} ([date] text, [temperature] text)'
        self.cursor.execute(query)
        self.conn.commit()

    def read_data(self, table_name):
        query = f'select * from {table_name}'
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def insert_data(self, table_name: str, data: list):
        query = f'insert into {table_name} values ("{data[0]}", "{data[1]}")'
        self.cursor.execute(query)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
