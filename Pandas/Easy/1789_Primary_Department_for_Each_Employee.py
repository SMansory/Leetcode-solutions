"""

Question: Primary department for each employee

Summary: Write a function to report all the employees with their primary department. 
For employees who belong to only one department, report their only department. Return the result table in any order.

Method: Group the employee DataFrame by 'employee_id' and count the number of unique 'department_id' values for each employee. 
Create a new column 'dept_cnt' with these counts. Filter the DataFrame to include rows where 'primary_flag' is 'Y' or
'dept_cnt' is 1. Select the 'employee_id' and 'department_id' columns from the filtered DataFrame.

Time complexity: O(n) 
Space complexity: O(n) 
"""

import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # Count the number of unique 'department_id' for each employee
    employee["dept_cnt"] = employee.groupby("employee_id")["department_id"].transform("nunique")
    # Filter rows where 'primary_flag' is 'Y' or 'dept_cnt' is 1
    return employee[(employee["primary_flag"] == "Y") | (employee["dept_cnt"] == 1)][["employee_id", "department_id"]]


# Example usage
data = {
    'employee_id': [1, 2, 2, 3, 4, 4, 4],
    'department_id': [1, 1, 2, 3, 2, 3, 4],
    'primary_flag': ['N', 'Y', 'N', 'N', 'N', 'Y', 'N']
}
employee = pd.DataFrame(data)

result = find_primary_department(employee)
print(result)
