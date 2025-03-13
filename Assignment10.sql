-- 1️⃣ Create a books table with columns (id, title, author, year_published)
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    year_published INT
);

-- 2️⃣ Insert at least 5 books into the table
INSERT INTO books (id, title, author, year_published) VALUES
(1, 'To Kill a Mockingbird', 'Harper Lee', 1960),
(2, '1984', 'George Orwell', 1949),
(3, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925),
(4, 'Pride and Prejudice', 'Jane Austen', 1813),
(5, 'The Catcher in the Rye', 'J.D. Salinger', 1951);

-- 3️⃣ Write queries to:

-- Select all books
SELECT * FROM books;

-- Get books by a specific author
SELECT * FROM books WHERE author = 'George Orwell';

-- Update the year of a book
UPDATE books SET year_published = 1961 WHERE id = 1;

-- Delete a book
DELETE FROM books WHERE id = 5;

-- 4️⃣ Challenge: Create a borrowers table and connect it to books using a foreign key

-- Create borrowers table
CREATE TABLE borrowers (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- Insert some borrowers
INSERT INTO borrowers (id, name, email, phone) VALUES
(1, 'John Smith', 'john@example.com', '555-1234'),
(2, 'Sarah Johnson', 'sarah@example.com', '555-5678'),
(3, 'Michael Brown', 'michael@example.com', '555-9012');

-- Create a loans table to connect books and borrowers
CREATE TABLE loans (
    id INT PRIMARY KEY,
    book_id INT,
    borrower_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
);

-- Insert some loan records
INSERT INTO loans (id, book_id, borrower_id, loan_date, return_date) VALUES
(1, 1, 2, '2023-10-01', '2023-10-15'),
(2, 3, 1, '2023-10-05', NULL),
(3, 2, 3, '2023-09-28', '2023-10-12');

-- Additional queries to demonstrate the relationship

-- Find all books borrowed by a specific borrower
SELECT b.title, b.author, l.loan_date, l.return_date
FROM books b
JOIN loans l ON b.id = l.book_id
WHERE l.borrower_id = 1;

-- Find all currently borrowed books (return_date is NULL)
SELECT b.title, b.author, br.name AS borrower
FROM books b
JOIN loans l ON b.id = l.book_id
JOIN borrowers br ON l.borrower_id = br.id
WHERE l.return_date IS NULL; 