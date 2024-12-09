-- Question: Reformat department table

-- Summary: Write a query that reformats the Department table so that there is a department 'id' column and a revenue column for each month.

-- Method: Use a SELECT statement with SUM(IF(...)) to calculate the total revenue for each month.
-- Use the GROUP BY clause to group by 'id'.

-- Create the Department table
CREATE TABLE Department (
    id INT,
    revenue INT,
    month VARCHAR(3)
);

-- Insert sample data into the Department table
INSERT INTO Department (id, revenue, month) VALUES
(1, 8000, 'Jan'),
(2, 9000, 'Jan'),
(3, 10000, 'Feb'),
(1, 7000, 'Feb'),
(1, 6000, 'Mar');

-- Query for the question
SELECT id, 
SUM(IF(month = "Jan", revenue, null)) as Jan_revenue, 
SUM(IF(month = "Feb", revenue, null)) as Feb_revenue,
SUM(IF(month = "Mar", revenue, null)) as Mar_revenue,
SUM(IF(month = "Apr", revenue, null)) as Apr_revenue,
SUM(IF(month = "May", revenue, null)) as May_revenue,
SUM(IF(month = "Jun", revenue, null)) as Jun_revenue,
SUM(IF(month = "Jul", revenue, null)) as Jul_revenue,
SUM(IF(month = "Aug", revenue, null)) as Aug_revenue,
SUM(IF(month = "Sep", revenue, null)) as Sep_revenue,
SUM(IF(month = "Oct", revenue, null)) as Oct_revenue,
SUM(IF(month = "Nov", revenue, null)) as Nov_revenue,
SUM(IF(month = "Dec", revenue, null)) as Dec_revenue
FROM department 
GROUP BY id;
