"""

Question: Recyclable and low fat products

Summary: Write a function to find the product 'IDs' of items that are both low fat and recyclable.

Method: Use the 'loc' method in pandas to filter rows where both 'low_fats' and 'recyclable' columns have the value 'Y', 
and return only the 'product_id' column.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products["low_fats"] == "Y") & (products["recyclable"] == "Y"), ["product_id"]]


# Example usage 
data = {'product_id': [101, 102, 103, 104, 105], 'low_fats': ['Y', 'N', 'Y', 'Y', 'N'], 'recyclable': ['Y', 'Y', 'N', 'Y', 'Y']} 
products = pd.DataFrame(data) 

result = find_products(products) 
print(result)
