-- Question: Triangle judgement

-- Summary: Write a query that reports whether every set of three line segments can form a triangle.

-- Method: Use a SELECT statement to retrieve all columns from the Triangle table. Use the IF function to check the triangle inequality theorem 
-- (sum of any two sides must be greater than the third side). If the condition is met, return 'Yes'; otherwise, return 'No'.

-- Create the Triangle table
CREATE TABLE Triangle (
    x INT,
    y INT,
    z INT
);

-- Insert sample data into the Triangle table
INSERT INTO Triangle (x, y, z) VALUES
(13, 15, 30),
(10, 20, 15);

-- Query for the question
SELECT *, IF((x + y > z) AND (x + z > y) AND (y + z > x), 'Yes', 'No') AS triangle 
FROM Triangle;
