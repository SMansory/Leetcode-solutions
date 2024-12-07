"""

Question: Customers who bought all products

Summary: Write a function that identifies customer IDs of customers who bought all the products listed in the Product table. 
Return the result table in any order.

Method: Group the 'customer' DataFrame by 'customer_id' and count the unique 'product_keys' for each customer.
Then filter customers who bought a number of unique products equal to the total number of products in the 'product' DataFrame.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Group by 'customer_id' and count unique 'product_keys'
    customer = customer.groupby(by="customer_id")["product_key"].nunique().reset_index()
    # Filter customers who bought all products
    return customer.loc[customer["product_key"] == len(product)][["customer_id"]]


# Example usage
customer_data = {
    'customer_id': [1, 2, 3, 3, 1],
    'product_key': [5, 6, 5, 6, 6]
}
product_data = {
    'product_key': [5, 6]
}

customer = pd.DataFrame(customer_data)
product = pd.DataFrame(product_data)

result = find_customers(customer, product)
print(result)
