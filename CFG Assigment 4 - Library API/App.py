from flask import Flask, request, jsonify
import MySQLdb
from db_utils import get_db_connection, create_tables

app = Flask(__name__)
create_tables()

@app.route('/books', methods=['GET'])
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    title = new_book.get('title')
    author = new_book.get('author')
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Book added successfully!'}), 201

@app.route('/books/borrow', methods=['POST'])
def borrow_book():
    book_id = request.get_json().get('id')
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT available FROM books WHERE id = %s", (book_id,))
    book = cursor.fetchone()
    if book and book[0]:
        cursor.execute("UPDATE books SET available = FALSE WHERE id = %s", (book_id,))
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({'message': 'Book borrowed successfully!'})
    else:
        cursor.close()
        connection.close()
        return jsonify({'message': 'Book not available!'}), 400

if __name__ == '__main__':
    app.run(debug=True)