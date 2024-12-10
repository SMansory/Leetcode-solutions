-- Question: Employees earning more than their managers

-- Summary: Write a query that finds employees who earn more than their managers. The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve the names of employees who earn more than their managers. 
-- Perform an INNER JOIN on the Employee table to link employees with their managers based on the 'managerId'. 
-- Use the WHERE clause to filter employees whose salaries are higher than their managers'.

-- Create the Employee table
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    salary INT,
    managerId INT
);

-- Insert sample data into the Employee table
INSERT INTO Employee (id, name, salary, managerId) VALUES
(1, 'Joe', 70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam', 60000, NULL),
(4, 'Max', 90000, NULL);

-- Query for the question
SELECT e1.name Employee 
FROM Employee AS e1 INNER JOIN Employee AS e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
