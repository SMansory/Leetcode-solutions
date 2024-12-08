-- Question: Rearrange products table

-- Summary: Write a query that rearranges the Products table so that each row has 'product_id', 'store', and 'price'. 
-- If a product is not available in a store, it should not be included in the result table.

-- Method: Use a series of SELECT statements combined with UNION to retrieve 'product_id', 'store' (aliased for each store), 
-- and 'price' from the Products table where the store's price is not NULL.

-- Create the Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    store1 INT,
    store2 INT,
    store3 INT
);

-- Insert sample data into the Products table
INSERT INTO Products (product_id, store1, store2, store3) VALUES
(0, 95, 100, 105),
(1, 70, NULL, 80);

-- Query for the question
SELECT product_id, 'store1' AS store, store1 AS price FROM Products
WHERE store1 IS NOT null
UNION
SELECT product_id, 'store2' AS store, store2 AS price FROM Products
WHERE store2 IS NOT null
UNION 
SELECT product_id, 'store3' AS store, store3 AS price FROM Products
WHERE store3 IS NOT null
