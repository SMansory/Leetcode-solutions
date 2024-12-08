-- Question: Number of unique subjects taught by each teacher

-- Summary: Write a query that calculates the number of unique subjects each teacher teaches in the university.
-- The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve 'teacher_id' and 
-- count the number of distinct 'subject_id' for each teacher using COUNT(DISTINCT subject_id). Group the result by 'teacher_id'.


-- Create the Teacher table
CREATE TABLE Teacher ( 
    teacher_id INT,  
    subject_id INT,
    dept_id INT 
);

-- Insert sample data into the Teacher table
INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES 
(1, 2, 3),
(1, 2, 4),
(1, 3, 3),  
(2, 1, 1),  
(2, 2, 1), 
(2, 3, 1), 
(2, 4, 1);

-- Query for the question 
# Write your MySQL query statement below
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt 
FROM Teacher
GROUP BY teacher_id
