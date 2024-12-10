-- Question: Employees whose manager left the company

-- Summary: Write a query that finds the IDs of employees whose salary is strictly less than $30000 and whose manager left the company. 
-- When a manager leaves, their information is deleted from the Employees table,
-- but the reports still have their 'manager_id' set to the manager that left. 
-- The result table should be ordered by 'employee_id'.

-- Method: Use a SELECT statement to retrieve 'employee_id' from the Employees table.
-- Apply the WHERE clause to filter employees with a salary less than $30000 and
-- whose 'manager_id' is not present in the Employees table.
-- Use the NOT IN clause to check for 'manager_id' not existing in the subquery of 'employee_id' from the Employees table.
-- Order the results by 'employee_id'.

-- Create the Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255),
    manager_id INT,
    salary INT
);

-- Insert sample data into the Employees table
INSERT INTO Employees (employee_id, name, manager_id, salary) VALUES
(3, 'Mila', 9, 60301),
(12, 'Antonella', NULL, 31000),
(13, 'Emery', NULL, 67084),
(1, 'Kalel', 11, 21241),
(9, 'Mikaela', NULL, 50937),
(11, 'Joziah', 6, 28485);

-- Solution for the question
SELECT employee_id 
FROM Employees
WHERE salary < 30000 AND manager_id NOT IN(SELECT employee_id FROM Employees)
ORDER BY employee_id;
