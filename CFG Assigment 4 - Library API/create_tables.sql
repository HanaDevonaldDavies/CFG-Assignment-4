-- Create table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2),
    published_date DATE
);

-- Sample data
INSERT INTO books (title, author, price, published_date)
VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 12.99, '1925-04-10');

INSERT INTO books (title, author, price, published_date)
VALUES ('To Kill a Mockingbird', 'Harper Lee', 10.50, '1960-07-11');

INSERT INTO books (title, author, price, published_date)
VALUES ('1984', 'George Orwell', 9.99, '1949-06-08');

INSERT INTO books (title, author, price, published_date)
VALUES ('Pride and Prejudice', 'Jane Austen', 7.95, '1813-01-28');

-- Retrieve books from table
SELECT * FROM books;