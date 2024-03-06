import os
import psycopg2
# Class to handle the database connection with docker


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(os.environ['DATABASE_URL'])

        # self.connection = psycopg2.connect(
        #     host=os.environ['POSTGRES_HOST'],
        #     database=os.environ['POSTGRES_DB'],
        #     user=os.environ['POSTGRES_USER'],
        #     password=os.environ['POSTGRES_PASSWORD']
        # )
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, name VARCHAR);")
        self.connection.commit()

    def list_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def add_user(self, name):
        self.cursor.execute(f"INSERT INTO users (name) VALUES ('{name}')")
        self.connection.commit()
        return True
