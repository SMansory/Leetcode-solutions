-- Question: Big countries

-- Summary: Write a query that finds the name, population, and area of countries that are considered "big."
-- A country is classified as big if it has an area of at least three million square kilometers or a population of at least twenty-five million.

-- Method: Use a SELECT statement to retrieve the 'name', 'population', and 'area' columns from the World table.
-- Apply the WHERE clause to filter countries that have a population of at least 25,000,000 or an area of at least 3,000,000 square kilometers.

-- Create the World table
CREATE TABLE World (
    name VARCHAR(255),
    continent VARCHAR(255),
    area INT,
    population INT,
    gdp BIGINT
);

-- Insert sample data into the World table
INSERT INTO World (name, continent, area, population, gdp) VALUES
('Afghanistan', 'Asia', 652230, 25500100, 20343000000),
('Albania', 'Europe', 28748, 2831741, 12960000000),
('Algeria', 'Africa', 2381741, 37100000, 188681000000),
('Andorra', 'Europe', 468, 78115, 3712000000),
('Angola', 'Africa', 1246700, 20609294, 100990000000);

-- Solution for the question
SELECT name, population, area 
FROM World
WHERE population >= 25000000 OR area >= 3000000;
