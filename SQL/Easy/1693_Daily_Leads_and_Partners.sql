-- Question: Daily leads and partners

-- Summary: Write a query that calculates the number of distinct 'lead_ids' and distinct 'partner_ids' for each 'date_id' and 'make_name'. 
-- The result can be returned in any order.

-- Method: Use a SELECT statement to retrieve 'date_id', 'make_name', and count the distinct 'lead_ids' and
-- 'partner_ids' for each combination of 'date_id' and 'make_name'. Group the result by 'date_id' and 'make_name'.

-- Create the DailySales table 
CREATE TABLE DailySales ( 
    date_id DATE, 
    make_name VARCHAR(255),
    lead_id INT,
    partner_id INT 
);

-- Insert sample data into the DailySales table 
INSERT INTO DailySales (date_id, make_name, lead_id, partner_id) VALUES 
('2020-12-8', 'toyota', 0, 1), 
('2020-12-8', 'toyota', 1, 0), 
('2020-12-8', 'toyota', 1, 2), 
('2020-12-7', 'toyota', 0, 2), 
('2020-12-7', 'toyota', 0, 1), 
('2020-12-8', 'honda', 1, 2), 
('2020-12-8', 'honda', 2, 1), 
('2020-12-7', 'honda', 0, 1), 
('2020-12-7', 'honda', 1, 2), 
('2020-12-7', 'honda', 2, 1);

-- Query for the question
SELECT date_id, make_name, COUNT(DISTINCT lead_id) AS unique_leads, COUNT(DISTINCT partner_id) AS unique_partners 
FROM DailySales
GROUP BY date_id, make_name;
