-- Question: Second highest salary

-- Summary: Write a query that finds the second highest distinct salary from the Employee table.
-- If there is no second highest salary, return null.

-- Method: Use a JOIN operation on the Employee table to compare salaries. 
-- The query finds the maximum salary from the Employee table where the salary is less than the highest salary. 
-- This effectively identifies the second highest distinct salary.

-- Create the Employee table
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    salary INT
);

-- Insert sample data into the Employee table
INSERT INTO Employee (id, salary) VALUES
(1, 100),
(2, 200),
(3, 300);

-- Solution for the question
SELECT MAX(e1.salary) AS SecondHighestSalary
FROM Employee AS e1 JOIN Employee AS e2 ON e1.salary < e2.salary;
