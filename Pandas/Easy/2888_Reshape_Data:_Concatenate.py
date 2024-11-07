"""

Question: Reshape data: concatenate

Summary: Write a function to concatenate two DataFrames vertically into one DataFrame.

Method: Use the 'merge' function in pandas to concatenate the DataFrames.

Time complexity: O(n + m) - Concatenating two DataFrames of sizes 'n' and 'm'.
Space complexity: O(n + m)
"""

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return df1.merge(df2, how = "outer")


# Example usage 
data1 = {'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']} 
data2 = {'id': [4, 5, 6], 'name': ['David', 'Eve', 'Frank'] } 

df1 = pd.DataFrame(data1) 
df2 = pd.DataFrame(data2) 

result = concatenateTables(df1, df2) 
print(result)
