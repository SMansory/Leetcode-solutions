-- Question: Bank account summary II

-- Summary: Write a query that reports the name and balance of users with a balance higher than 10000.
-- The balance of an account is calculated as the sum of the amounts of all transactions involving that account.

-- Method: Use a SELECT statement to retrieve 'name' and the sum of 'amount' (aliased as 'balance') from the Users and Transactions tables. 
-- Join the tables on the 'account' column. Group the result by 'account' and filter using HAVING to include only those with a balance greater than 10000.

-- Create the Users table
CREATE TABLE Users (
    account INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the Transactions table
CREATE TABLE Transactions (
    trans_id INT,
    account INT,
    amount INT,
    transacted_on DATE
);

-- Insert sample data into the Users table
INSERT INTO Users (account, name) VALUES
(900001, 'Alice'),
(900002, 'Bob'),
(900003, 'Charlie');

-- Insert sample data into the Transactions table
INSERT INTO Transactions (trans_id, account, amount, transacted_on) VALUES
(1, 900001, 7000, '2020-08-01'),
(2, 900001, 7000, '2020-09-01'),
(3, 900001, -3000, '2020-09-02'),
(4, 900002, 1000, '2020-09-12'),
(5, 900003, 6000, '2020-08-07'),
(6, 900003, 6000, '2020-09-07'),
(7, 900003, -4000, '2020-09-11');

-- Query for the question
SELECT name, SUM(amount) AS balance 
FROM Users AS u JOIN Transactions AS t ON u.account = t.account
GROUP BY t.account
HAVING SUM(t.amount) > 10000;
