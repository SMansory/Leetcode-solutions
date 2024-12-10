-- Question: Top travellers

-- Summary: Write a query that reports the distance traveled by each user. 
-- The result table is ordered by 'travelled_distance' in descending order,
-- and if two or more users traveled the same distance, they are ordered by their name in ascending order.

-- Method: Use a SELECT statement to retrieve the 'name' of the user and the sum of the distance traveled 
-- (aliased as 'travelled_distance'). Perform a LEFT JOIN with the Rides table on the 'user_id' column.
-- Use the IF function to handle NULL distances by replacing them with 0.
-- Group the results by 'user_id' and order by 'travelled_distance' in descending order, and 'name' in ascending order.

-- Create the Users table
CREATE TABLE Users (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the Rides table
CREATE TABLE Rides (
    id INT PRIMARY KEY,
    user_id INT,
    distance INT
);

-- Insert sample data into the Users table
INSERT INTO Users (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Alex'),
(4, 'Donald'),
(7, 'Lee'),
(13, 'Jonathan'),
(19, 'Elvis');

-- Insert sample data into the Rides table
INSERT INTO Rides (id, user_id, distance) VALUES
(1, 1, 120),
(2, 2, 317),
(3, 3, 222),
(4, 7, 100),
(5, 13, 312),
(6, 19, 50),
(7, 7, 120),
(8, 19, 400),
(9, 7, 230);

-- Solution for the question
SELECT u.name, SUM(IF(distance IS NULL, 0, distance)) AS travelled_distance 
FROM Users AS u LEFT JOIN Rides AS r ON u.id = r.user_id
GROUP BY user_id
ORDER BY travelled_distance DESC, name ASC;
