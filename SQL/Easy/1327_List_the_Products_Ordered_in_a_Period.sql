-- Question: List the products ordered in a period

-- Summary: Write a query that retrieves the names of products that have at least 100 units ordered in February 2020 and their total units.

-- Method: Use a SELECT statement to join the Products and Orders tables on the 'product_id' column.
-- Filter the results to only include orders placed in February 2020.
-- Use the GROUP BY clause to group the results by 'product_name' and the HAVING clause to only include products with at least 100 units ordered.

-- Create the Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    product_category VARCHAR(255)
);

-- Create the Orders table
CREATE TABLE Orders (
    product_id INT,
    order_date DATE,
    unit INT
);

-- Insert sample data into the Products table
INSERT INTO Products (product_id, product_name, product_category) VALUES
(1, 'Leetcode Solutions', 'Book'),
(2, 'Jewels of Stringology', 'Book'),
(3, 'HP', 'Laptop'),
(4, 'Lenovo', 'Laptop'),
(5, 'Leetcode Kit', 'T-shirt');

-- Insert sample data into the Orders table
INSERT INTO Orders (product_id, order_date, unit) VALUES
(1, '2020-02-05', 60),
(1, '2020-02-10', 70),
(2, '2020-01-18', 30),
(2, '2020-02-11', 80),
(3, '2020-02-17', 2),
(3, '2020-02-24', 3),
(4, '2020-03-01', 20),
(4, '2020-03-04', 30),
(4, '2020-03-04', 60),
(5, '2020-02-25', 50),
(5, '2020-02-27', 50),
(5, '2020-03-01', 50);

-- Query for the question
SELECT product_name, SUM(unit) AS unit 
FROM Products AS p LEFT JOIN Orders AS o ON p.product_id = o.product_id
WHERE (YEAR(order_date) = 2020 AND MONTH(order_date) = 02) 
GROUP BY product_name HAVING (unit >= 100);
