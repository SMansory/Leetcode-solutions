"""

Question: Number of unique subjects taught by each teacher

Summary: Write a function to calculate the number of unique subjects each teacher teaches at a university.

Method: Use the 'groupby' method in pandas to group by 'teacher_id', 
then calculate the number of unique 'subject_id' values for each teacher. Reset the index and rename the resulting column.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby("teacher_id")["subject_id"].nunique().reset_index().rename(columns = {"subject_id": "cnt"})


# Example usage 
data = {'teacher_id': [1, 1, 1, 2, 2, 2, 2], 'subject_id': [2, 2, 3, 1, 2, 3, 4], 'dept_id': [3, 4, 3, 1, 1, 1, 1]} 
teacher = pd.DataFrame(data) 

result = count_unique_subjects(teacher) 
print(result)
