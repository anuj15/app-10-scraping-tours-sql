import sqlite3


class DBManager:

    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(database=db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str):
        query = f'create table if not exists {table_name} ([band_name] text, [city_name] text, [date] text)'
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, data: list):
        query = f'insert into {table_name} values ("{data[0]}", "{data[1]}", "{data[2]}")'
        self.cursor.execute(query)
        self.conn.commit()

    def get_data(self, table):
        query = f'select * from {table}'
        result = self.cursor.execute(query)
        return result.fetchall()

    def close_connection(self):
        self.conn.close()
