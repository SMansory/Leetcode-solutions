"""

Question: Employees with missing information

Summary: Write a function to report the IDs of all the employees with missing information.
The information of an employee is missing if their name is missing or their salary is missing. 
Return the result table ordered by 'employee_id' in ascending order.

Method: Merge the 'employees' and 'salaries' tables on 'employee_id' using an outer join to ensure 
all records from both tables are included. Filter the rows where 'name' or 'salary' is missing. 
Sort the result by 'employee_id' in ascending order and select the 'employee_id' column.

Time complexity: O(n log n) - Sorting the DataFrame. 
Space complexity: O(n)
"""

import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    # Merge 'employees' and 'salaries' tables on 'employee_id' using outer join
    merged_table = employees.merge(salaries, on = "employee_id", how = "outer")
    # Filter rows where 'name' or 'salary' is missing
    result = merged_table[merged_table["name"].isna() | merged_table["salary"].isna()].sort_values(by = "employee_id")[["employee_id"]]
    return result


# Example usage
employees_data = {
    'employee_id': [2, 4, 5],
    'name': ['Crew', 'Haven', 'Kristian']
}
salaries_data = {
    'employee_id': [5, 1, 4],
    'salary': [76071, 22517, 63539]
}

employees = pd.DataFrame(employees_data)
salaries = pd.DataFrame(salaries_data)

result = find_employees(employees, salaries)
print(result)
