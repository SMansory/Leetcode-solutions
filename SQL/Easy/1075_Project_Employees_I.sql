-- Question: Project employees I

-- Summary: Write a query that reports the average experience years of all the employees for each project,
-- rounded to 2 decimal places. The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve the 'project_id' and the average 'experience_years' (aliased as 'average_years') for each project. 
-- Perform an INNER JOIN with the Employee table on the 'employee_id' column. 
-- Use the ROUND function to round the average experience years to 2 decimal places. Group the results by 'project_id'.

-- Create the Project table
CREATE TABLE Project (
    project_id INT,
    employee_id INT
);

-- Create the Employee table
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255),
    experience_years INT
);

-- Insert sample data into the Project table
INSERT INTO Project (project_id, employee_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4);

-- Insert sample data into the Employee table
INSERT INTO Employee (employee_id, name, experience_years) VALUES
(1, 'Khaled', 3),
(2, 'Ali', 2),
(3, 'John', 1),
(4, 'Doe', 2);

-- Solution for the question
SELECT project_id, ROUND(AVG(1.00 * experience_years), 2) AS average_years 
FROM Project AS p INNER JOIN Employee AS e ON p.employee_id = e.employee_id
GROUP BY project_id;
