-- Question: Find followers count

-- Summary: Write a query that returns the number of followers for each user. 
-- The result table should be ordered by 'user_id' in ascending order.

-- Method: Use a SELECT statement to retrieve 'user_id' and the count of 'follower_id' (aliased as 'followers_count') from the Followers table.
-- Group the results by 'user_id' and order by 'user_id' in ascending order.

-- Create the Followers table
CREATE TABLE Followers (
    user_id INT,
    follower_id INT
);

-- Insert sample data into the Followers table
INSERT INTO Followers (user_id, follower_id) VALUES
(0, 1),
(1, 0),
(2, 0),
(2, 1);

-- Solution for the question
SELECT user_id, COUNT(follower_id) AS followers_count 
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC;
