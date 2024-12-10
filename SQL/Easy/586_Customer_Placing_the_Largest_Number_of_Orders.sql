-- Question: Customer placing the largest number of orders

-- Summary: This query finds the 'customer_number' for the customer who has placed the largest number of orders.

-- Method: Use a SELECT statement to retrieve the 'customer_number' from the Orders table.
-- Group the results by 'customer_number' and order them by the count of 'order_number' in descending order.
-- Use the LIMIT clause to ensure only one result (the customer with the most orders) is returned.

-- Create the Orders table
CREATE TABLE Orders (
    order_number INT PRIMARY KEY,
    customer_number INT
);

-- Insert sample data into the Orders table
INSERT INTO Orders (order_number, customer_number) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 3);

-- Solution for the question
SELECT customer_number 
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;
