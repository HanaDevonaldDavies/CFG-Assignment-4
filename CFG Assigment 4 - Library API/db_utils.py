import mysql.connector
from config import *

# Establish database connection
def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Fetch books from database
def fetch_all_books():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
        cursor.close()
        connection.close()
        return books
    except Exception as e:
        raise e

# Insert a new book 
def insert_book(title, author, price, published_date):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        insert_query = 'INSERT INTO books (title, author, price, published_date) VALUES (%s, %s, %s, %s)'
        cursor.execute(insert_query, (title, author, price, published_date))
        connection.commit()
        book_id = cursor.lastrowid
        cursor.close()
        connection.close()
        return book_id
    except Exception as e:
        raise e

# Fetch all authors from database
def fetch_all_authors():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT DISTINCT author FROM books')
        authors = [author['author'] for author in cursor.fetchall()]
        cursor.close()
        connection.close()
        return authors
    except Exception as e:
        raise e