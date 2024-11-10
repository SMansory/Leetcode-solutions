"""

Question: Reshape data: pivot

Summary: Write a function to pivot the data so that each row represents temperatures for a specific month,
and each city is a separate column.

Method: Use the 'pd.pivot_table' function in pandas to reshape the DataFrame, with 'month' as the index, 
'city' as the columns, and 'temperature' as the values. Use 'max' as the aggregation function.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # Pivot the table so that each row represents temperatures for a specific month, and each city is a separate column
    return pd.pivot_table(weather, index = "month", columns = "city", values = "temperature", aggfunc = "max")


# Example usage
data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May', 'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}
weather = pd.DataFrame(data)

result = pivotTable(weather)
print(result)
