-- Question: Customers who never order

-- Summary: Write a query that finds all customers who never ordered anything. The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve the 'name' column from the Customers table.
-- Perform a LEFT JOIN with the Orders table on the 'customerId' column. 
-- Use the WHERE clause to filter out customers who have no orders (i.e., where 'customerId' in the Orders table is NULL).

-- Create the Customers table
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the Orders table
CREATE TABLE Orders (
    id INT PRIMARY KEY,
    customerId INT
);

-- Insert sample data into the Customers table
INSERT INTO Customers (id, name) VALUES
(1, 'Joe'),
(2, 'Henry'),
(3, 'Sam'),
(4, 'Max');

-- Insert sample data into the Orders table
INSERT INTO Orders (id, customerId) VALUES
(1, 3),
(2, 1);

-- Solution for the question
SELECT name AS Customers 
FROM Customers AS c LEFT JOIN Orders AS o ON c.id = o.customerId
WHERE o.customerId IS NULL;
