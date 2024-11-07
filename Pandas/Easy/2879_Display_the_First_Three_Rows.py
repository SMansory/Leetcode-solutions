"""

Question: Display the first three rows

Summary: Write a solution to display the first 3 rows of a given DataFrame.

Method: Use the 'head' method in pandas to select the first 3 rows of the DataFrame.

Time complexity: O(1)
Space complexity: O(1)
"""

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


# Example usage 
data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 'Age': [23, 34, 45, 29, 30]} 
employees = pd.DataFrame(data) 

result = selectFirstRows(employees) 
print(result)
