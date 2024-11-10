"""

Question: Replace employee id with the unique identifier

Summary: Write a function to show the unique ID of each user. If a user does not have a unique ID, display null.

Method: Use the 'merge' method in pandas to join the 'employees' and 'employee_uni' tables on the 'id' column, 
using a left join to include all employees. Select the columns 'unique_id' and 'name' from the merged DataFrame.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Merge the 'employees' and 'employee_uni' tables on 'id' using a left join and select the required columns
    return employees.merge(employee_uni, how = "left", on = "id")[["unique_id", "name"]]


# Example usage
employees_data = {
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
}
employee_uni_data = {
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
}

employees = pd.DataFrame(employees_data)
employee_uni = pd.DataFrame(employee_uni_data)

result = replace_employee_id(employees, employee_uni)
print(result)
