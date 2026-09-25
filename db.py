import psycopg2
from config import DB_CONFIG


def get_connection():

    try:

        connection = psycopg2.connect(
            **DB_CONFIG
        )

        print("Database connected successfully!")

        return connection

    except psycopg2.Error as error:

        print("Database connection failed!")

        print(error)

        return None