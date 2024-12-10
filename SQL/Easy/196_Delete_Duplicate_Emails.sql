-- Question: Delete duplicate emails

-- Summary: Write a query that deletes all duplicate emails in the Person table, keeping only one unique email with the smallest 'id'.

-- Method: Use a DELETE statement to remove duplicate emails from the Person table. 
-- Perform a JOIN operation on the Person table to match rows with the same email.
-- Use the WHERE clause to filter out rows where the 'id' is greater than the 'id' of another row with the same email, 
-- ensuring that only the row with the smallest 'id' is kept. 

-- Create the Person table
CREATE TABLE Person (
    id INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL
);

-- Insert sample data into the Person table
INSERT INTO Person (id, email) VALUES
(1, 'john@example.com'),
(2, 'bob@example.com'),
(3, 'john@example.com');

-- Solution for the question
DELETE p1 
FROM Person AS p1 JOIN Person AS p2 ON p1.email = p2.email
WHERE p1.email = p2.email AND p1.id > p2.id;
