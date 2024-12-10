-- Question: Patients with a condition

-- Summary: Write a query that finds the 'patient_id', 'patient_name', and 'conditions' of the patients who have Type I Diabetes.
-- Type I Diabetes always starts with the DIAB1 prefix. 
-- The result table can be returned in any order.

-- Method: Use a SELECT statement to retrieve all columns from the Patients table. 
-- Apply the WHERE clause to filter rows where the 'conditions' column contains the DIAB1 prefix. 
-- Use the LIKE operator to handle cases where DIAB1 is either at the beginning or appears within the conditions string.

-- Create the Patients table
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(255),
    conditions VARCHAR(255)
);

-- Insert sample data into the Patients table
INSERT INTO Patients (patient_id, patient_name, conditions) VALUES
(1, 'Daniel', 'YFEV COUGH'),
(2, 'Alice', ''),
(3, 'Bob', 'DIAB100 MYOP'),
(4, 'George', 'ACNE DIAB100'),
(5, 'Alain', 'DIAB201');

-- Solution for the question
SELECT * FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%';
