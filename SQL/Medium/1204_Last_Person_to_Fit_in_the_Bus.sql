-- Question: Last person to fit in the bus

-- Summary: Write a query that finds the 'person_name' of the last person that can fit on the bus without exceeding the weight limit of 1000 kilograms. 
-- Each person boards the bus in the order specified by the 'turn' column.

-- Method: Use a subquery to calculate the running total weight (w) for each person as they board the bus, 
-- ordered by the 'turn' column. Use the SUM function with the OVER clause to get the cumulative weight.
-- Filter the results in the outer query to only include those whose cumulative weight is less than or equal to 1000 kilograms.
-- Order the results by the cumulative weight in descending order and limit the output to the last person who can fit on the bus.

-- Create the Queue table
CREATE TABLE Queue (
    person_id INT PRIMARY KEY,
    person_name VARCHAR(255),
    weight INT,
    turn INT
);

-- Insert sample data into the Queue table
INSERT INTO Queue (person_id, person_name, weight, turn) VALUES
(5, 'Alice', 250, 1),
(4, 'Bob', 175, 5),
(3, 'Alex', 350, 2),
(6, 'John Cena', 400, 3),
(1, 'Winston', 500, 6),
(2, 'Marie', 200, 4);

-- Solution for the question
SELECT person_name FROM (SELECT person_name, SUM(weight) OVER(ORDER BY turn) AS w 
FROM Queue) q
WHERE w<= 1000
ORDER BY w DESC 
LIMIT 1;
