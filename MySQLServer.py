#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",      # change if your MySQL is remote
            user="root",           # replace with your MySQL username
            password="your_password"  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()
