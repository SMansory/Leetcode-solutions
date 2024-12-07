-- Question: Recyclable and low fat products

-- Summary: Write a query that finds the 'product_id' of products that are both low fat and
-- recyclable. The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve 'product_id' from the Products table
-- where both 'low_fats' and 'recyclable' columns have a value of 'Y'.

-- Create the Products table 
CREATE TABLE Products ( 
    product_id INT PRIMARY KEY, 
    low_fats CHAR(1), 
    recyclable CHAR(1) 
); 

-- Insert sample data into the Products table 
INSERT INTO Products (product_id, low_fats, recyclable) VALUES 
(0, 'Y', 'N'), 
(1, 'Y', 'Y'),
(2, 'N', 'Y'), 
(3, 'Y', 'Y'), 
(4, 'N', 'N');

-- Query for the question
SELECT product_id FROM Products
WHERE low_fats ='Y' AND recyclable = 'Y';
