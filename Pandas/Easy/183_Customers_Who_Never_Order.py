"""

Question: Customers who never order

Summary: Write a function to find all customers who never order anything. Return the result table in any order.

Method: Use the 'isin' method in pandas to filter the customers DataFrame to exclude customers
who have an entry in the orders DataFrame. Rename the 'name' column to 'Customers' and select this column.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Filter customers who never ordered anything
    result = customers[~customers["id"].isin(orders["customerId"])]
    # Rename the 'name' column to 'Customers'
    result = result.rename(columns = {"name": "Customers"})[["Customers"]]
    return result


# Example usage
customers_data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}
orders_data = {
    'id': [1, 2],
    'customerId': [3, 1]
}

customers = pd.DataFrame(customers_data)
orders = pd.DataFrame(orders_data)

result = find_customers(customers, orders)
print(result)
