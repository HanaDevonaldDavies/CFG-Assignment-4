# CFG-Assignment-4
## Bookshop API
This project implements a simple Flask API for managing books and authors in a bookstore. It includes endpoints to retrieve all books, add new books, and retrieve all authors from a MySQL database.

*** My 'MySQL' is still not connecting properly to a server, I have tried to fix it many times but it only gives me error codes. If there are any issues with the SQL side of the assignment let me know and I'll try my best to write a new code or send you the file. I have attached pictures of the codes as well as the files themeselves just in case :). I'm going to try and get my laptop checked out to sort out the issue asap, Sorry for any inconvenience.***

### Installation and Editing 
1. Clone the Repository from https://github.com/HanaDevonaldDavies/CFG-Assignment-4.git
2. Install Python and all requirements listed in requirements.txt file
3. Database
   Create SQL database 'Bookshop' and create a table of books
4. Configuration
   Update DB_HOST, DB_USER, DB_PASSWORD, and DB_NAME with your MySQL database credentials.
   
### Running the API
1. Start the Flask server:
   Run the Flask application (app.py)
2. API Endpoints:

- GET /books: Retrieve all books from the database.
- POST /books: Add a new book to the database.
- GET /authors: Retrieve all authors from the database.

### Example API Interactions
- Retrieve all books
- Add new books
- Retrieve all authors
- Retrieve all publishing dates
