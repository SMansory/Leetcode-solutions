-- Question: Classes more than 5 students

-- Summary: Write a query that finds all the classes that have at least five students.
-- The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve the 'class' column from the Courses table. 
-- Group the results by 'class' and use the HAVING clause to filter groups with a count of student greater than or equal to 5.

-- Create the Courses table
CREATE TABLE Courses (
    student VARCHAR(255),
    class VARCHAR(255)
);

-- Insert sample data into the Courses table
INSERT INTO Courses (student, class) VALUES
('A', 'Math'),
('B', 'English'),
('C', 'Math'),
('D', 'Biology'),
('E', 'Math'),
('F', 'Computer'),
('G', 'Math'),
('H', 'Math'),
('I', 'Math');

-- Solution for the question
SELECT class 
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
