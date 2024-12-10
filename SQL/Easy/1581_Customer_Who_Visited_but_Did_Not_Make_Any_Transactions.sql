-- Question: Customer who visited but did not make any transactions

-- Summary: Write a query that finds the IDs of users who visited without making any transactions and the number of such visits. 
-- The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve 'customer_id' and the count of visits without transactions 
-- (aliased as 'count_no_trans') from the Visits table. Perform a LEFT JOIN with the Transactions table on the 'visit_id' column.
-- Use the WHERE clause to filter visits that have no corresponding transaction (t.'visit_id' IS NULL). 
-- Group the results by 'customer_id'.

-- Create the Visits table
CREATE TABLE Visits (
    visit_id INT PRIMARY KEY,
    customer_id INT
);

-- Create the Transactions table
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    visit_id INT,
    amount INT
);

-- Insert sample data into the Visits table
INSERT INTO Visits (visit_id, customer_id) VALUES
(1, 23),
(2, 9),
(4, 30),
(5, 54),
(6, 96),
(7, 54),
(8, 54);

-- Insert sample data into the Transactions table
INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES
(2, 5, 310),
(3, 5, 300),
(9, 5, 200),
(12, 1, 910),
(13, 2, 970);

-- Solution for the question
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits AS v LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;
