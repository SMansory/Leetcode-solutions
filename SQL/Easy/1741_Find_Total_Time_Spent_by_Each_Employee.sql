-- Question: Find total time spent by each employee

-- Summary: Write a query that calculates the total time in minutes spent by each employee on each day at the office. 
-- The time spent in the office for a single entry is calculated as (out_time - in_time).

-- Method: Use a SELECT statement to retrieve 'event_day' (aliased as day), 'emp_id', and 
-- the sum of the differences between 'out_time' and 'in_time' for each employee on each day. 
-- Group the result by 'event_day' and 'emp_id'.

-- Create the Employees table 
CREATE TABLE Employees ( 
    emp_id INT,  
    event_day DATE, 
    in_time INT, 
    out_time INT 
);

-- Insert sample data into the Employees table 
INSERT INTO Employees (emp_id, event_day, in_time, out_time) VALUES 
(1, '2020-11-28', 4, 32), 
(1, '2020-11-28', 55, 200)
(1, '2020-12-03', 1, 42), 
(2, '2020-11-28', 3, 33),
(2, '2020-12-09', 47, 74);

-- Query for the question
SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
