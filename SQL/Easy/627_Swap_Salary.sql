-- Question: Swap salary

-- Summary: Write a query that swaps all 'f' and 'm' values in the 'gender' column of the salary table.
-- A single UPDATE statement can be used, without any intermediate temporary tables.

-- Method: Use an UPDATE statement with a CASE expression to change 'f' values to 'm' and vice versa in the 'gender' column.

-- Create the Salary table
CREATE TABLE salary (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    gender CHAR(1),
    salary INT
);

-- Insert sample data into the Salary table
INSERT INTO salary (id, name, gender, salary) VALUES
(1, 'A', 'm', 2500),
(2, 'B', 'f', 1500),
(3, 'C', 'm', 5500),
(4, 'D', 'f', 500);

-- Query for the question
UPDATE salary
SET gender = (CASE WHEN gender = "f" THEN "m" ELSE "f" END)
