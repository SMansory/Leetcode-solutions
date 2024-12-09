-- Question: Employee bonus

-- Summary: Write a query that reports the name and bonus amount of each employee with a bonus less than 1000. 
-- If an employee does not have a bonus, show it as NULL.

-- Method: Use a LEFT JOIN to combine the Employee and Bonus tables on the 'empId' column.
-- Use the WHERE clause to filter out rows where the bonus is less than 1000 or is NULL.

-- Create the Employee table
CREATE TABLE Employee (
    empId INT PRIMARY KEY,
    name VARCHAR(255),
    supervisor INT,
    salary INT
);

-- Create the Bonus table
CREATE TABLE Bonus (
    empId INT PRIMARY KEY,
    bonus INT
);

-- Insert sample data into the Employee table
INSERT INTO Employee (empId, name, supervisor, salary) VALUES
(3, 'Brad', NULL, 4000),
(1, 'John', 3, 1000),
(2, 'Dan', 3, 2000),
(4, 'Thomas', 3, 4000);

-- Insert sample data into the Bonus table
INSERT INTO Bonus (empId, bonus) VALUES
(2, 500),
(4, 2000);

-- Query for the question
SELECT name, bonus 
FROM Employee AS e LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE bonus < 1000 or bonus IS null;
