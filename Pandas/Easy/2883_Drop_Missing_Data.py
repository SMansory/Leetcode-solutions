"""

Question: Drop missing data

Summary: Write a function to remove the rows with missing values in the 'name' column.

Method: Use the 'dropna' method in pandas to drop rows from the 'students' DataFrame where the 'name' column has missing values.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Remove rows with missing values in the 'name' column
    return students.dropna(subset = ["name"])


# Example usage
data = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}
students = pd.DataFrame(data)

result = dropMissingData(students)
print(result)
