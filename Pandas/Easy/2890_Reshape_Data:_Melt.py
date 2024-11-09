"""

Question: Reshape data: melt

Summary: Write a function to reshape the data so that each row represents sales data for a product in a specific quarter.

Method: Use the 'pd.melt' function to reshape the DataFrame, with product as the identifier variable, 
quarter as the variable name, and sales as the value name.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars = "product", var_name = "quarter", value_name = "sales")


# Example usage 
data = {'product': ['Umbrella', 'SleepingBag'], 'quarter_1': [417, 800], 'quarter_2': [224, 936], 'quarter_3': [379, 93], 'quarter_4': [611, 875]} 
report = pd.DataFrame(data) 

result = meltTable(report) 
print(result)
