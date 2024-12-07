"""

Question: Department highest salary

Summary: Write a function that identifies the employees who have the highest salary in each department. 
Return the result in any order.

Method: First, merge the 'employee' and 'department' DataFrames on the department IDs.
Then, group the merged DataFrame by Department and find the maximum salary in each group. 
Finally, filter the DataFrame to include only those rows where the salary matches the maximum salary for the respective department.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge the 'employee' and 'department' DataFrames
    df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left')
    # Rename columns for clarity
    df = df.rename(columns={'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})[['Department', 'Employee', 'Salary']]
    # Find the employees with the highest salary in each department
    return df[df['Salary'] == df.groupby('Department')['Salary'].transform(max)]


# Example usage
employee_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}
department_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}

employee = pd.DataFrame(employee_data)
department = pd.DataFrame(department_data)

result = department_highest_salary(employee, department)
print(result)
