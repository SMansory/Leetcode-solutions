-- Question: Actors and directors who cooperated at least three times

-- Summary: Write a query that finds all the pairs of 'actor_id' and 'director_id' where the actor has cooperated with the director at least three times.
-- The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve 'actor_id' and 'director_id' from the ActorDirector table.
-- Group the results by 'actor_id' and 'director_id'. 
-- Use the HAVING clause to filter groups with a count of timestamp greater than or equal to 3.

-- Create the ActorDirector table
CREATE TABLE ActorDirector (
    actor_id INT,
    director_id INT,
    timestamp INT
);

-- Insert sample data into the ActorDirector table
INSERT INTO ActorDirector (actor_id, director_id, timestamp) VALUES
(1, 1, 0),
(1, 1, 1),
(1, 1, 2),
(1, 2, 3),
(1, 2, 4),
(2, 1, 5),
(2, 1, 6);

-- Query for the question
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(timestamp) >= 3;
