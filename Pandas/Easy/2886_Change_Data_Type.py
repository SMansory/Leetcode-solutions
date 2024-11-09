"""

Question: Change data type

Summary: Write a function to correct the errors in the DataFrame. Specifically,
convert the grade column from floats to integers.

Method: Convert the 'grade' column to integers using the 'astype' method in pandas.

Time complexity: O(n) 
Space complexity: O(1)
"""

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    # Convert the 'grade' column to integers
    students["grade"] = students["grade"].astype(int)
    return students


# Example usage 
data = {'student_id': [1, 2], 'name': ['Ava', 'Kate'], 'age': [6, 15], 'grade': [73.0, 87.0]} 
students = pd.DataFrame(data) 

students = changeDatatype(students) 
print(students)
