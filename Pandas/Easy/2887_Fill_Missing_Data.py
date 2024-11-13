"""

Question: Fill missing data 

Summary: Write a function to fill in the missing values as 0 in the 'quantity' column.

Method: Use the 'assign' method in pandas to update the 'quantity' column, replacing None values with 0 using 'fillna'.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # Fill missing values in the 'quantity' column with 0
    return products.assign(quantity=products["quantity"].fillna(0))


# Example usage
data = {
    'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
    'quantity': [None, None, 779, 849],
    'price': [135, 821, 9319, 3051]
}
products = pd.DataFrame(data)

result = fillMissingValues(products)
print(result)
