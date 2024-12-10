-- Question: Rising temperature

-- Summary: Write a query that finds all dates' IDs where the temperature is higher compared to the previous date (yesterday).
-- The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve the 'id' of dates where the temperature is higher than the previous date. 
-- Perform a JOIN operation on the Weather table to compare the temperatures of adjacent days.
-- Use the DATEDIFF function to ensure the comparison is made between consecutive days.

-- Create the Weather table
CREATE TABLE Weather (
    id INT PRIMARY KEY,
    recordDate DATE,
    temperature INT
);

-- Insert sample data into the Weather table
INSERT INTO Weather (id, recordDate, temperature) VALUES
(1, '2015-01-01', 10),
(2, '2015-01-02', 25),
(3, '2015-01-03', 20),
(4, '2015-01-04', 30);

-- Solution for the question
SELECT W1.id 
FROM Weather AS w1 JOIN Weather AS w2 
WHERE w1.temperature > w2.temperature AND DATEDIFF(w1.recordDate, w2.recordDate) = 1;
