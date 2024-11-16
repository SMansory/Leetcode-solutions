"""

Question: Project employees I

Summary: Write a function that reports the average experience years of all the employees for each project, rounded to 2 digits.
Return the result table in any order.

Method: Merge the 'project' and 'employee' DataFrames on 'employee_id' using a left join. 
Group the merged DataFrame by 'project_id' and calculate the mean of 'experience_years'. 
Round the average experience years to 2 decimal places, reset the index,
and rename the 'experience_years' column to 'average_years'.

Time complexity: O(n)  
Space complexity: O(n)
"""

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    # Merge 'project' and 'employee' tables on 'employee_id' using left join
    result = project.merge(employee, on = "employee_id", how = "left")
    # Group by 'project_id' and calculate the average experience years
    result =  result.groupby("project_id")["experience_years"].mean().round(2).reset_index()
    # Rename the 'experience_years' column to 'average_years'
    result = result.rename(columns = {"experience_years": "average_years"})
    return result


# Example usage
project_data = {
    'project_id': [1, 1, 1, 2, 2],
    'employee_id': [1, 2, 3, 1, 4]
}
employee_data = {
    'employee_id': [1, 2, 3, 4],
    'name': ['Khaled', 'Ali', 'John', 'Doe'],
    'experience_years': [3, 2, 1, 2]
}

project = pd.DataFrame(project_data)
employee = pd.DataFrame(employee_data)

result = project_employees_i(project, employee)
print(result)
