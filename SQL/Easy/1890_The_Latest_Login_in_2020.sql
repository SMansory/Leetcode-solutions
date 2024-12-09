-- Question: The latest login in 2020

-- Summary: Write a query that reports the latest login for all users in the year 2020. 
-- Users who did not log in during 2020 should be excluded from the result.

-- Method: Use a SELECT statement to retrieve 'user_id' and the maximum 'time_stamp' for each user in the year 2020.
-- Use the WHERE clause to filter logins that occurred in 2020. Group the result by 'user_id'.

-- Create the Logins table
CREATE TABLE Logins (
    user_id INT,
    time_stamp DATETIME
);

-- Insert sample data into the Logins table
INSERT INTO Logins (user_id, time_stamp) VALUES
(6, '2020-06-30 15:06:07'),
(6, '2021-04-21 14:06:06'),
(6, '2019-03-07 00:18:15'),
(8, '2020-02-01 05:10:53'),
(8, '2020-12-30 00:46:50'),
(2, '2020-01-16 02:49:50'),
(2, '2019-08-25 07:59:08'),
(14, '2019-07-14 09:00:00'),
(14, '2021-01-06 11:59:59');

-- Query for the question
SELECT user_id, MAX(time_stamp) AS last_stamp 
FROM Logins
WHERE year(time_stamp) = 2020
GROUP BY user_id;
