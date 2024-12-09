-- Question: Combine two tables

-- Summary: Write a query that reports the first name, last name, city, and state of each person in the Person table. 
-- If the address of a 'personId' is not present in the Address table, report it NULL.

-- Method: Use a LEFT JOIN to combine the Person and Address tables on the 'personId' column.
-- Select the 'firstName', 'lastName', 'city', and 'state' columns from the joined tables.

-- Create the Person table
CREATE TABLE Person (
    personId INT PRIMARY KEY,
    lastName VARCHAR(255),
    firstName VARCHAR(255)
);

-- Create the Address table
CREATE TABLE Address (
    addressId INT PRIMARY KEY,
    personId INT,
    city VARCHAR(255),
    state VARCHAR(255)
);

-- Insert sample data into the Person table
INSERT INTO Person (personId, lastName, firstName) VALUES
(1, 'Wang', 'Allen'),
(2, 'Alice', 'Bob');

-- Insert sample data into the Address table
INSERT INTO Address (addressId, personId, city, state) VALUES
(1, 2, 'New York City', 'New York'),
(2, 3, 'Leetcode', 'California');

-- Query for the question
SELECT firstName, lastName, city, state 
FROM Person AS p LEFT JOIN Address AS a ON p.personId = a.personId;
