import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # change to your MySQL username
            password="password"   # change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection closed")

if __name__ == "__main__":
    create_database()
