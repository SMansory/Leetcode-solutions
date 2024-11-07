"""

Question: Modify columns

Summary: A company aims to give its employees a pay rise. 
Write a solution to modify the salary column by multiplying each salary by 2.

Method: Use the 'assign' method in pandas to modify the salary column.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(salary = 2 * employees["salary"])


# Example usage 
data = {'employee_id': [1, 2, 3], 'name': ['John', 'Alice', 'Bob'], 'salary': [50000, 60000, 70000]} 
employees = pd.DataFrame(data) 

result = modifySalaryColumn(employees)
print(result)
