"""

Question: Customer placing the largest number of orders

Summary: Write a function to find the 'customer_number' for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.

Method: Group the orders DataFrame by 'customer_number' and count the number of 'order_number' for each customer. 
Reset the index to get a DataFrame. Filter this DataFrame to include only the row(s) with the maximum order count.
Select the 'customer_number' column from the filtered DataFrame.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by 'customer_number' and count the number of orders
    max_orders = orders.groupby("customer_number")["order_number"].count().reset_index()
    # Filter to get the customer with the maximum number of orders
    max_orders = max_orders[max_orders["order_number"] == max_orders["order_number"].max()]
    # Select the 'customer_number' column
    return max_orders[["customer_number"]]


# Example usage
data = {
    'order_number': [1, 2, 3, 4],
    'customer_number': [1, 2, 3, 3]
}
orders = pd.DataFrame(data)

result = largest_orders(orders)
print(result)
