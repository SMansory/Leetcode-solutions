-- Question: Duplicate emails

-- Summary: Write a query that reports all duplicate emails in the Person table. 
-- It's guaranteed that the email field is not NULL, and the result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve 'email' from the Person table.
-- Group the results by 'email' and use the HAVING clause to filter groups with a count greater than 1,
-- indicating duplicate emails.

-- Create the Person table
CREATE TABLE Person (
    id INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL
);

-- Insert sample data into the Person table
INSERT INTO Person (id, email) VALUES
(1, 'a@b.com'),
(2, 'c@d.com'),
(3, 'a@b.com');

-- Query for the question
SELECT email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
