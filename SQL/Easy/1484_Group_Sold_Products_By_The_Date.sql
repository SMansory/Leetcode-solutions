-- Question: Group sold products by the date

-- Summary: Write a query that finds the number of different products sold and their names for each date.
-- The product names are sorted lexicographically. The result table should be ordered by 'sell_date'.

-- Method: Use a SELECT statement to retrieve 'sell_date', count the distinct products, and concatenate the product names.
-- Use the GROUP BY clause to group by 'sell_date'. The GROUP_CONCAT function with DISTINCT is used to concatenate product names, 
-- and the ORDER BY clause in the GROUP_CONCAT function sorts the product names lexicographically.

-- Create the Activities table
CREATE TABLE Activities (
    sell_date DATE,
    product VARCHAR(255)
);

-- Insert sample data into the Activities table
INSERT INTO Activities (sell_date, product) VALUES
('2020-05-30', 'Headphone'),
('2020-06-01', 'Pencil'),
('2020-06-02', 'Mask'),
('2020-05-30', 'Basketball'),
('2020-06-01', 'Bible'),
('2020-06-02', 'Mask'),
('2020-05-30', 'T-Shirt');

-- Query for the question
# Write your MySQL query statement below
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, group_concat(DISTINCT product) AS products 
FROM Activities
GROUP BY sell_date;
