-- Question: Article views I

-- Summary: Write a query that finds all the authors that viewed at least one of their own articles.
-- The result table should be sorted by 'id' in ascending order.

-- Method: Use a SELECT statement to retrieve distinct 'author_id' values where the 'author_id' is equal to the 'viewer_id'.
-- Use the ORDER BY clause to sort the result by 'id' in ascending order.

-- Create the Views table
CREATE TABLE Views (
    article_id INT,
    author_id INT,
    viewer_id INT,
    view_date DATE
);

-- Insert sample data into the Views table
INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
(1, 3, 5, '2019-08-01'),
(1, 3, 6, '2019-08-02'),
(2, 7, 7, '2019-08-01'),
(2, 7, 6, '2019-08-02'),
(4, 7, 1, '2019-07-22'),
(3, 4, 4, '2019-07-21'),
(3, 4, 4, '2019-07-21');

-- Query for the question
SELECT  DISTINCT author_id AS id 
FROM Views 
WHERE author_id = viewer_id
ORDER BY id;
