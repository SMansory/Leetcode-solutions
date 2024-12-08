-- Question: Replace employee ID with the unique identifier

-- Summary: Write a query that displays the unique ID of each user from the Employees table.
-- If a user does not have a unique ID in the EmployeeUNI table, it shows NULL.

-- Method: Use a LEFT JOIN to combine the Employees and EmployeeUNI tables on the 'id' column.
-- Select the 'unique_id' and 'name' columns from the joined tables.

-- Create the Employees table
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the EmployeeUNI table
CREATE TABLE EmployeeUNI (
    id INT PRIMARY KEY,
    unique_id INT
);

-- Insert sample data into the Employees table
INSERT INTO Employees (id, name) VALUES
(1, 'Alice'),
(7, 'Bob'),
(11, 'Meir'),
(90, 'Winston'),
(3, 'Jonathan');

-- Insert sample data into the EmployeeUNI table
INSERT INTO EmployeeUNI (id, unique_id) VALUES
(3, 1),
(11, 2),
(90, 3);

-- Query for the question
SELECT unique_id, name 
FROM Employees AS e1 LEFT JOIN EmployeeUNI AS e2 ON e1.id = e2.id;
