"""

Question: Swap salary

Summary: Write a function to swap all 'f' and 'm' values in a DataFrame 
(i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.

Method: Use the 'replace' method in pandas to swap 'f' with 'm' and 'm' with 'f'.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    # Replace 'f' with 'm' and 'm' with 'f' in the 'gender' column
    return salary.replace({"f":"m", "m":"f"})


# Example usage
data = {
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'gender': ['m', 'f', 'm', 'f'],
    'salary': [2500, 1500, 5500, 500]
}

salary = pd.DataFrame(data)

result = swap_salary(salary)
print(result)
