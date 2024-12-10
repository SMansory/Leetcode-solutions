-- Question: Find customer referee

-- Summary: Write a query that retrieves the names of customers who are not referred by the customer with 'id' = 2.
-- The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve the 'name' column from the Customer table.
-- Use the WHERE clause to filter out customers whose 'referee_id' is 2 or is NULL.

-- Create the Customer table
CREATE TABLE Customer (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    referee_id INT
);

-- Insert sample data into the Customer table
INSERT INTO Customer (id, name, referee_id) VALUES
(1, 'Will', NULL),
(2, 'Jane', NULL),
(3, 'Alex', 2),
(4, 'Bill', NULL),
(5, 'Zack', 1),
(6, 'Mark', 2);

-- Query for the question
SELECT name 
FROM Customer
WHERE referee_id != 2 or referee_id is NULL;
