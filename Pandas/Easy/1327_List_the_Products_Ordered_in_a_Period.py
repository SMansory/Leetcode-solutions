"""

Question: List the products ordered in a period

Summary: Write a function to get the names of products that have at least 100 units ordered in February 2020 and their amount.
Return the result table in any order.

Method: Filter the orders DataFrame to include only the rows where the 'order_date' is in February 2020.
Group the filtered orders by 'product_id' and sum the unit values. 
Filter this grouped result to include only products with at least 100 units. 
Merge this result with the products DataFrame to get the product names and select the 'product_name' and 'unit' columns.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Filter orders for February 2020 and group by 'product_id' to sum units
    orders = orders[(orders["order_date"].dt.year == 2020) & (orders["order_date"].dt.month == 2)].groupby(["product_id"])["unit"].sum().reset_index()
    # Filter products with at least 100 units ordered and merge with 'products' DataFrame to get product names
    return orders[orders["unit"] >= 100].merge(products[["product_id", "product_name"]])[["product_name", "unit"]]


# Example usage
products_data = {
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Leetcode Solutions', 'Jewels of Stringology', 'HP', 'Lenovo', 'Leetcode Kit'],
    'product_category': ['Book', 'Book', 'Laptop', 'Laptop', 'T-shirt']
}
orders_data = {
    'product_id': [1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5],
    'order_date': pd.to_datetime(['2020-02-05', '2020-02-10', '2020-01-18', '2020-02-11', '2020-02-17', '2020-02-24', '2020-03-01', '2020-03-04', '2020-03-04', '2020-02-25', '2020-02-27', '2020-03-01']),
    'unit': [60, 70, 30, 80, 2, 3, 20, 30, 60, 50, 50, 50]
}

products = pd.DataFrame(products_data)
orders = pd.DataFrame(orders_data)

result = list_products(products, orders)
print(result)
