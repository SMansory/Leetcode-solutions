"""

Question: Employee bonus

Summary: Write a function to report the name and bonus amount of each employee with a bonus less than 1000. 
Return the result table in any order.

Method: Merge the 'employee' and 'bonus' tables on 'empId' using an outer join. 
Filter the rows to include only those with a bonus less than 1000 or no bonus at all.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merge 'employee' and 'bonus' tables on 'empId' using outer join
    bonus = employee.merge(bonus, on = "empId", how = "outer")
    # Filter rows with bonus less than 1000 or no bonus
    filt = bonus[(bonus["bonus"] < 1000) | (bonus["bonus"].isna())]
    return filt[["name", "bonus"]]


# Example usage
employee_data = {
    'empId': [3, 1, 2, 4],
    'name': ['Brad', 'John', 'Dan', 'Thomas'],
    'supervisor': [None, 3, 3, 3],
    'salary': [4000, 1000, 2000, 4000]
}
bonus_data = {
    'empId': [2, 4],
    'bonus': [500, 2000]
}

employee = pd.DataFrame(employee_data)
bonus = pd.DataFrame(bonus_data)

result = employee_bonus(employee, bonus)
print(result)
