"""

Question: Product sales analysis I

Summary: Write a function to report the 'product_name', 'year', and 'price' for each 'sale_id' in the Sales table.

Method: Use the 'merge' method in pandas to join the Sales and Products tables on 'product_id', 
then select the columns 'product_name', 'year', and 'price' from the merged DataFrame.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Merge the Sales and Product tables on 'product_id' and select the required columns
    return sales.merge(product, on = "product_id")[["product_name", "year", "price"]]


# Example usage 
sales_data = { 
  'sale_id': [1, 2, 7], 
  'product_id': [100, 100, 200], 
  'year': [2008, 2009, 2011], 
  'quantity': [10, 12, 15], 
  'price': [5000, 5000, 9000] 
} 
product_data = { 
  'product_id': [100, 200], 
  'product_name': ['Product A', 'Product B'] 
} 

sales = pd.DataFrame(sales_data) 
product = pd.DataFrame(product_data) 

result = sales_analysis(sales, product) 
print(result)
