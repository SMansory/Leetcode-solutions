-- Question: Employees with missing information

-- Summary: Write a query that reports the IDs of all employees with missing information. 
-- The information of an employee is considered missing if the employee's name or salary is not present. 
-- The result table should be ordered by 'employee_id' in ascending order.

-- Method: Use two subqueries with the SELECT statement to identify 'employee_ids' missing from either the Employees or Salaries table.
-- Combine the results using UNION and order the final result by 'employee_id' in ascending order.

-- Create the Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the Salaries table
CREATE TABLE Salaries (
    employee_id INT PRIMARY KEY,
    salary INT
);

-- Insert sample data into the Employees table
INSERT INTO Employees (employee_id, name) VALUES
(2, 'Crew'),
(4, 'Haven'),
(5, 'Kristian');

-- Insert sample data into the Salaries table
INSERT INTO Salaries (employee_id, salary) VALUES
(5, 76071),
(1, 22517),
(4, 63539);

-- Query for the question
SELECT employee_id 
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id 
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id ASC;
