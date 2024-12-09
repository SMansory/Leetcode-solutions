-- Question: Not boring movies

-- Summary: Write a query that reports the movies with an odd-numbered ID and a description that is not "boring". 
-- The result table should be ordered by 'rating' in descending order.

-- Method: Use a SELECT statement to retrieve all columns from the Cinema table where the 'description' is not "boring" and the 'id' is odd.
-- Use the ORDER BY clause to sort the result by 'rating' in descending order.

-- Create the Cinema table
CREATE TABLE Cinema (
    id INT PRIMARY KEY,
    movie VARCHAR(255),
    description VARCHAR(255),
    rating DECIMAL(3, 1)
);

-- Insert sample data into the Cinema table
INSERT INTO Cinema (id, movie, description, rating) VALUES
(1, 'War', 'great 3D', 8.9),
(2, 'Science', 'fiction', 8.5),
(3, 'irish', 'boring', 6.2),
(4, 'Ice song', 'Fantacy', 8.6),
(5, 'House card', 'Interesting', 9.1);

-- Query for the question
SELECT * FROM Cinema
WHERE (description != 'boring') AND (id % 2 != 0)
ORDER BY rating DESC;
