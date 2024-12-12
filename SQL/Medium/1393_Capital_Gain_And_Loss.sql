-- Question: Capital gain and loss

-- Summary: Write a query that reports the capital gain or loss for each stock by calculating the total gain or loss after buying and 
-- selling the stock one or many times. The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve the 'stock_name' and calculate the capital gain or loss (aliased as 'capital_gain_loss').
-- Use the CASE statement within the SUM function to add the 'price' if the operation is "Sell" and
-- subtract the 'price' if the operation is "Buy". Group the results by 'stock_name'.

-- Create the Stocks table
CREATE TABLE Stocks (
    stock_name VARCHAR(255),
    operation VARCHAR(255),
    operation_day INT,
    price INT
);

-- Insert sample data into the Stocks table
INSERT INTO Stocks (stock_name, operation, operation_day, price) VALUES
('Leetcode', 'Buy', 1, 1000),
('Corona Masks', 'Buy', 2, 10),
('Leetcode', 'Sell', 5, 9000),
('Handbags', 'Buy', 17, 30000),
('Corona Masks', 'Sell', 3, 1010),
('Corona Masks', 'Buy', 4, 1000),
('Corona Masks', 'Sell', 5, 500),
('Corona Masks', 'Buy', 6, 1000),
('Handbags', 'Sell', 29, 7000),
('Corona Masks', 'Sell', 10, 10000);

-- Solution for the question
SELECT stock_name, SUM(CASE WHEN operation = "Sell" THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
