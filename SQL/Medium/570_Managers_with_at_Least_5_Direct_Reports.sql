-- Question: Managers with at least 5 Direct reports

-- Summary: Write a query that finds the names of managers who have at least five direct reports. 
-- The result table can be returned in any order.

-- Method: Use a subquery to group employees by m'anagerId' and filter for those with at least five direct reports (HAVING count(id) >= 5).
-- Use the IN clause to find the names of employees whose 'id' matches the 'managerId' from the subquery.

-- Create the Employee table
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255),
    managerId INT
);

-- Insert sample data into the Employee table
INSERT INTO Employee (id, name, department, managerId) VALUES
(101, 'John', 'A', NULL),
(102, 'Dan', 'A', 101),
(103, 'James', 'A', 101),
(104, 'Amy', 'A', 101),
(105, 'Anne', 'A', 101),
(106, 'Ron', 'B', 101);

-- Solution for the question
SELECT name 
FROM Employee
WHERE id IN (SELECT managerId FROM Employee GROUP BY managerId HAVING count(id) >= 5);
