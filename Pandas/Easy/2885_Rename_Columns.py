"""

Question: Rename columns

Summary: Write a function to rename the columns of a DataFrame as follows: 'id' to 'student_id', 'first' to 'first_name', 
'last' to 'last_name', and 'age' to 'age_in_years'.

Method: Use the 'rename' method in pandas to rename the columns based on a specified mapping dictionary.

Time complexity: O(1) 
Space complexity: O(1)
"""

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # Mapping of old column names to new column names
    student = {
        "id": "student_id",
        "first": "first_name",
        "last": "last_name",
        "age": "age_in_years"
    }
    # Rename the columns based on the mapping
    return students.rename(columns=student)


# Example usage 
data = {
  'id': [1, 2, 3, 4, 5], 
  'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'], 
  'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'], 
  'age': [6, 7, 16, 18, 10] 
} 
students = pd.DataFrame(data) 

result = renameColumns(students)
print(result)
