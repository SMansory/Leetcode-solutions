"""

Question: Employees whose manager left the company

Summary: Write a function that identifies employees whose salary is less than $30,000 and whose manager has left the company.
Order the result table by 'employee_id'.

Method: Filter the 'employees' DataFrame to find employees with salaries less than $30,000 and
whose 'manager_id' does not exist in the 'employee_id' column (indicating the manager has left).
Return the filtered DataFrame ordered by 'employee_id'.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Filter employees with salary < 30000 and 'manager_id' not in 'employee_id', sort by 'employee_id' and select the 'employee_id' column
    return employees[(employees["salary"] < 30000) & ~(employees.manager_id.isin(employees.employee_id))].dropna().sort_values("employee_id")[["employee_id"]]


# Example usage
employees_data = {
    'employee_id': [3, 12, 13, 1, 9, 11],
    'name': ['Mila', 'Antonella', 'Emery', 'Kalel', 'Mikaela', 'Joziah'],
    'manager_id': [9, None, None, 11, None, 6],
    'salary': [60301, 31000, 67084, 21241, 50937, 28485]
}
employees = pd.DataFrame(employees_data)

result = find_employees(employees)
print(result)
