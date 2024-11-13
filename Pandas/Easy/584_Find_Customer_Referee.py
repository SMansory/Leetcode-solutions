"""

Question: Find customer referee

Summary: Write a function to find the names of customers that are not referred by the customer with 'id' = 2.
Return the result table in any order.

Method: Filter the DataFrame to include only the rows where 'referee_id' is not equal to 2 or is NULL. 
Select the 'name' column from the filtered DataFrame.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where 'referee_id' is not 2 or is NULL
    return customer[(customer["referee_id"] != 2) | (customer["referee_id"].isna())][["name"]]


# Example usage
data = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
    'referee_id': [None, None, 2, None, 1, 2]
}
customer = pd.DataFrame(data)

result = find_customer_referee(customer)
print(result)
