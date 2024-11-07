"""

Question: Create a new column

Summary: Write a function to add a new column bonus to a DataFrame,
containing values that are double the values in the salary column.

Method: Create a new column bonus by multiplying the values in the salary column by 2.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 2 * employees["salary"]
    return employees


# Example usage 
data = {'employee_id': [1, 2, 3], 'name': ['John', 'Alice', 'Bob'], 'salary': [50000, 60000, 70000]} 
employees = pd.DataFrame(data)

result = createBonusColumn(employees) 
print(result)
