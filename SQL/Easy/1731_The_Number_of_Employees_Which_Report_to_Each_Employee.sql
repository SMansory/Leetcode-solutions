-- Question: The number of employees which report to each employee 

-- Summary: Write a query that reports the IDs and names of all managers, the number of employees who report directly to them,
-- and the average age of the reports rounded to the nearest integer. The result table should be ordered by 'employee_id'.

-- Method: Use a SELECT statement to retrieve the 'employee_id', 'name', the count of direct reports (aliased as 'reports_count'), 
-- and the rounded average age of the reports (aliased as 'average_age'). 
-- Perform a JOIN operation on the Employees table to link employees with their managers based on the 'reports_to' column. 
-- Use the GROUP BY clause to group the results by 'employee_id' and the HAVING clause to filter groups with at least one report.
-- Order the results by 'employee_id'.

-- Create the Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255),
    reports_to INT,
    age INT
);

-- Insert sample data into the Employees table
INSERT INTO Employees (employee_id, name, reports_to, age) VALUES
(9, 'Hercy', NULL, 43),
(6, 'Alice', 9, 41),
(4, 'Bob', 9, 36),
(2, 'Winston', NULL, 37);

-- Solution for the question
SELECT e1.employee_id, e1.name, COUNT(e2.employee_id) AS reports_count, ROUND(AVG(e2.age)) AS average_age 
FROM Employees AS e1 JOIN Employees AS e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
HAVING reports_count > 0
ORDER BY e1.employee_id;
