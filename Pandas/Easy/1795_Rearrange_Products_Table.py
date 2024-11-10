"""

Question: Rearrange products table

Summary: Write a function to rearrange the Products table so that each row has ('product_id', store, price). 
If a product is not available in a store, do not include that 'product_id' and store combination in the result table.

Method: Use the 'pd.melt' function to reshape the DataFrame, with 'product_id' as the identifier variable, 
store as the variable name, and price as the value name. Use dropna to remove rows where the price is NaN.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Reshape the DataFrame
    return pd.melt(products, id_vars = "product_id", var_name = "store", value_name = "price").dropna()


# Example usage
data = {
    'product_id': [0, 1],
    'store1': [95, 70],
    'store2': [100, None],
    'store3': [105, 80]
}
products = pd.DataFrame(data)

result = rearrange_products_table(products)
print(result)
