-- Question: Odd and even transactions

-- Summary: Write a query that calculates the sum of amounts for odd and even transactions for each day.
-- If there are no odd or even transactions for a specific date, it displays 0 for that type.
-- The result table should be ordered by 'transaction_date' in ascending order.

-- Method: Use a SELECT statement to retrieve the 'transaction_date' and calculate the sum of odd and even amounts 
-- (aliased as 'odd_sum' and 'even_sum' respectively). 
-- Use the IF function within the SUM function to sum the amounts where the condition for odd or even is met.
-- Group the results by 'transaction_date' and order them by 'transaction_date'.

-- Create the Transactions table
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    amount INT,
    transaction_date DATE
);

-- Insert sample data into the Transactions table
INSERT INTO Transactions (transaction_id, amount, transaction_date) VALUES
(1, 150, '2024-07-01'),
(2, 200, '2024-07-01'),
(3, 75, '2024-07-01'),
(4, 300, '2024-07-02'),
(5, 50, '2024-07-02'),
(6, 120, '2024-07-03');

-- Solution for the question
SELECT transaction_date, 
SUM(if(amount % 2 = 1, amount, 0)) AS odd_sum, 
SUM(if(amount % 2 = 0, amount, 0)) AS even_sum 
FROM Transactions
GROUP BY transaction_date
ORDER BY transaction_date;
