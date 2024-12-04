"""

Question: Calculate special bonus

Summary: Write a function that calculates the bonus of each employee.
An employee receives a bonus equivalent to 100% of their salary if their employee ID is an odd number and
their name does not start with the character 'M'. Otherwise, the bonus is 0. 
You can return the result in order by 'employee_id'.

Method: Create a new column 'bonus' in the employees DataFrame, initially set to the value of the 'salary' column.
Update the 'bonus' column to 0 for employees with an even 'employee_id' or whose names start with 'M'.
Return the DataFrame sorted by 'employee_id'.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Initially set the 'bonus' to the 'salary'
    employees["bonus"] = employees["salary"]
    # Set 'bonus' to 0 if 'employee_id' is even or name starts with 'M'
    employees.loc[(employees["employee_id"] % 2 == 0) | (employees["name"].str[0] == "M"), "bonus"] = 0
    # Sort the DataFrame by 'employee_id'
    return employees[["employee_id", "bonus"]].sort_values("employee_id")


# Example usage
employees_data = {
    'employee_id': [2, 3, 7, 8, 9],
    'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
    'salary': [3000, 3800, 7400, 6100, 7700]
}
employees = pd.DataFrame(employees_data) 

result = calculate_special_bonus(employees)
print(result)
