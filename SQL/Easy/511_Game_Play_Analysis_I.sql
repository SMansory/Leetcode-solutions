-- Question: Game play analysis I

-- Summary: Write a query that finds the first login date for each player. The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve 'player_id' and 
-- the minimum 'event_date' (aliased as 'first_login') from the Activity table.
-- Use the GROUP BY clause to group the results by 'player_id'.

-- Create the Activity table
CREATE TABLE Activity (
    player_id INT,
    device_id INT,
    event_date DATE,
    games_played INT
);

-- Insert sample data into the Activity table
INSERT INTO Activity (player_id, device_id, event_date, games_played) VALUES
(1, 2, '2016-03-01', 5),
(1, 2, '2016-05-02', 6),
(2, 3, '2017-06-25', 1),
(3, 1, '2016-03-02', 0),
(3, 4, '2018-07-03', 5);

-- Query for the question
SELECT player_id, MIN(event_date) AS first_login 
FROM Activity
GROUP BY player_id;
