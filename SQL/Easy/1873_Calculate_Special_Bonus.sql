-- Question: Calculate special bonus

-- Summary: Write a query that calculates the bonus of each employee.
-- The bonus is 100% of their salary if the employee's ID is an odd number and their name does not start with the character 'M'. 
-- The bonus is 0 otherwise.

-- Method: Use a SELECT statement to retrieve the 'employee_id' and calculate the bonus. 
-- Use the IF function to check if the 'employee_id' is odd and the 'name' does not start with 'M'. If both conditions are met, 
-- the bonus is the employee's salary; otherwise, the bonus is 0. Order the result by 'employee_id' in ascending order.

-- Create the Employees table
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(255),
    salary INT
);

-- Insert sample data into the Employees table
INSERT INTO Employees (employee_id, name, salary) VALUES
(2, 'Meir', 3000),
(3, 'Michael', 3800),
(7, 'Addilyn', 7400),
(8, 'Juan', 6100),
(9, 'Kannon', 7700);

-- Solution for the question
SELECT employee_id, IF(employee_id % 2 = 0 OR name LIKE "M%", 0, salary) AS bonus 
FROM Employees
ORDER BY employee_id ASC;
