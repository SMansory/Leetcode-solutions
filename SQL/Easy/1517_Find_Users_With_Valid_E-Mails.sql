-- Question: Find users with valid e-mails

-- Summary: Write a query that finds the users who have valid emails. A valid email has a prefix name that starts with a letter and may contain 
-- letters, digits, underscore '_', period '.', and/or dash '-'.  The domain must be '@leetcode.com'.

-- Method: Use a SELECT statement to retrieve all columns from the Users table. 
-- Apply the WHERE clause to filter emails that match the regex pattern for a valid email.

-- Create the Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name VARCHAR(255),
    mail VARCHAR(255)
);

-- Insert sample data into the Users table
INSERT INTO Users (user_id, name, mail) VALUES
(1, 'Winston', 'winston@leetcode.com'),
(2, 'Jonathan', 'jonathanisgreat'),
(3, 'Annabelle', 'bella-@leetcode.com'),
(4, 'Sally', 'sally.come@leetcode.com'),
(5, 'Marwan', 'quarz#2020@leetcode.com'),
(6, 'David', 'david69@gmail.com'),
(7, 'Shapiro', '.shapo@leetcode.com');

-- Solution for the question
SELECT * FROM Users
WHERE mail REGEXP "^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$";
