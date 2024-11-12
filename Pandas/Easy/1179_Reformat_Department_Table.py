"""

Question: Reformat department table

Summary: Write a function to reformat the table so that there is a department ID column and a revenue column for each month.
Return the result table in any order.

Method: Use the 'pivot' method in pandas to reshape the DataFrame, setting 'id' as the index, 'month' as the columns, 
and 'revenue' as the values. Reindex the columns to ensure all months are included, even if they have no revenue. 
Rename the columns to include "_Revenue" for clarity and reset the index.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # Pivot the table
    monthRevenue = department.pivot(index = "id", columns = "month", values = "revenue")
    # Ensure all months are included
    monthRevenue = monthRevenue.reindex(columns = months)
    # Rename columns for clarity
    monthRevenue.rename(columns = lambda months: months + "_Revenue", inplace = True)
    # Reset index
    monthRevenue.reset_index(inplace = True)
    return monthRevenue


# Example usage
data = {
    'id': [1, 2, 3, 1, 1],
    'revenue': [8000, 9000, 10000, 7000, 6000],
    'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar']
}
department = pd.DataFrame(data)

result = reformat_table(department)
print(result)
