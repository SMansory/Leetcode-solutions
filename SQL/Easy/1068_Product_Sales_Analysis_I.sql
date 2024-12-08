-- Question: Product sales analysis I

-- Summary: Write a query that reports the 'product_name', 'year', and 'price' for each 'sale_id' in the Sales table.
-- The result table can be returned in any order.

-- Method: Use an INNER JOIN to combine the Sales and Product tables on the 'product_id' column.
-- Select the 'product_name', 'year', and 'price' columns from the joined tables.

-- Create the Sales table
CREATE TABLE Sales (
    sale_id INT,
    product_id INT,
    year INT,
    quantity INT,
    price INT
);

-- Create the Product table
CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255)
);

-- Insert sample data into the Sales table
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2008, 10, 5000),
(2, 100, 2009, 12, 5000),
(7, 200, 2011, 15, 9000);

-- Insert sample data into the Product table
INSERT INTO Product (product_id, product_name) VALUES
(100, 'Nokia'),
(200, 'Apple'),
(300, 'Samsung');

-- Query for the question
SELECT product_name, year, price 
FROM Sales AS s INNER JOIN Product AS p ON s.product_id = p.product_id;
