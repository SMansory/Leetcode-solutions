"""

Question: Select data

Summary: Write a function to select the name and age of the student with 'student_id' = 101.

Method: Use the 'loc' method in pandas to filter the DataFrame for the row with 'student_id' = 101 and 
select the 'name' and 'age' columns.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # Select the 'name' and 'age' of the student with 'student_id' = 101
    return students.loc[students["student_id"] == 101, ["name", "age"]]


# Example usage
data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}
students = pd.DataFrame(data)

result = selectData(students)
print(result)
