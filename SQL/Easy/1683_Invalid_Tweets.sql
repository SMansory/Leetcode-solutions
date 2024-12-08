-- Question: Invalid tweets

-- Summary: Write a query that finds the IDs of invalid tweets.
-- A tweet is considered invalid if the content's character length is strictly greater than 15.

-- Method: Use a SELECT statement to retrieve 'tweet_id' from the Tweets table where the LENGTH(content) is greater than 15.

-- Create the Tweets table
CREATE TABLE Tweets (
    tweet_id INT PRIMARY KEY,
    content VARCHAR(255)
);

-- Insert sample data into the Tweets table
INSERT INTO Tweets (tweet_id, content) VALUES
(1, 'Let us Code'),
(2, 'More than fifteen chars are here!');

-- Query for the question
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;
