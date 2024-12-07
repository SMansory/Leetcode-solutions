"""

Question: Managers with at least 5 direct reports

Summary: Write a function that identifies managers who have at least five direct reports. You can return the result in any order.

Method: First, count the occurrences of each 'managerId' in the 'employee' DataFrame. 
Then, filter for managers who have at least five direct reports. Finally, return the names of these managers.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Count the occurrences of each 'managerId'
    df = employee['managerId'].value_counts()
    # Find managers with at least five direct reports
    return employee.loc[employee['id'].isin(df[df >= 5].index), ['name']]


# Example usage
employee_data = {
    'id': [101, 102, 103, 104, 105, 106],
    'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
    'department': ['A', 'A', 'A', 'A', 'A', 'B'],
    'managerId': [None, 101, 101, 101, 101, 101]
}
employee = pd.DataFrame(employee_data)

result = find_managers(employee)
print(result)
