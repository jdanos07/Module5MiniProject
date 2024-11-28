Database Integration with MySQL:

Integrate a MySQL database into the Library Management System to store and retrieve data related to books, users, authors, and genres.

Design and create the necessary database tables to represent these entities. You will align these tables with the object-oriented structure from the previous project.

Establish connections between Python and the MySQL database for data manipulation, enhancing the persistence and scalability of your Library Management System.

Data Definition Language Scripts:

Create the necessary database tables for the Library Management System. For instance:

Books Table:
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id),
);

Authors Table:
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

Users Table:
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

Borrowed Books Table:
CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
