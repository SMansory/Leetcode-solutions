-- Question: Biggest single number

-- Summary: Writeba query that finds the largest number that appears only once in the MyNumbers table.
-- If there is no such number, report it  NULL.

-- Method: Use a subquery to select numbers that appear only once by grouping the 'num' column and using the HAVING clause to filter groups with a count of 1. 
-- Then, use the MAX function to find the largest number from the subquery results.

-- Create the MyNumbers table
CREATE TABLE MyNumbers (
    num INT
);

-- Insert sample data into the MyNumbers table
INSERT INTO MyNumbers (num) VALUES
(8),
(8),
(3),
(3),
(1),
(4),
(5),
(6);

-- Solution for the question
SELECT MAX(num) AS num FROM (
    SELECT num 
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1) AS num;
