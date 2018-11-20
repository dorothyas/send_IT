import psycopg2
import os

class Connection:
    """class handles Database connection"""

    def __init__(self):
        # try:
        #     postgres_db = 'send_it'

        #     if os.getenv('SETTING') == 'testing':
        #         postgres_bd='postgres'

        self.connection = psycopg2.connect(dbname= 'sendit',
                                        user='postgres',
                                        password='dorothy',
                                        host='localhost',
                                        port='5432'
                                        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        print('Connected to database')

        # except Exception as error:
        #     print(error)

    def create_tables(self):
        """ This method creates tables in the PostgreSQL database"""

        table = "CREATE TABLE IF NOT EXISTS users ( user_id SERIAL PRIMARY KEY, \
            user_name VARCHAR(10), user_email VARCHAR(100), contact INTEGER, user_password VARCHAR(100), \
            admin BOOLEAN NOT NULL);"
        self.cursor.execute(table)
        
        table = "CREATE TABLE IF NOT EXISTS orders \
			( order_id SERIAL PRIMARY KEY, parcel_type VARCHAR(15), weight INTEGER, receiver VARCHAR(15), \
            pick_up VARCHAR(15), destination VARCHAR(15), status VARCHAR(15), present_location VARCHAR(15), \
            user_id INTEGER) ;"
        self.cursor.execute(table)

    def drop_tables(self):
        """method deletes tables"""

        drop_user_table = "DROP TABLE users cascade"
        drop_orders_table = "DROP TABLE orders cascade"
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_orders_table) 

# Connection().create_tables()

