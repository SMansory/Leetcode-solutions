"""

Question: Create a dataFrame from list

Summary: Write a function to create a DataFrame from a 2D list called 'student_data', 
which contains the IDs and ages of some students. The DataFrame should have two columns, 'student_id' and 'age', 
and be in the same order as the original 2D list.

Method: Use the 'pd.DataFrame' constructor to create a DataFrame from the 2D list, 
specifying the column names as 'student_id' and 'age'.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    # Create DataFrame from the 2D list with specified column names
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df


# Example usage
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

df = createDataframe(student_data)
print(df)
