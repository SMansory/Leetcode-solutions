"""

Question: Drop duplicate rows

Summary: Write a function to remove duplicate rows in a DataFrame based on the email column and
keep only the first occurrence of each email.

Method: Use the 'drop_duplicates' method in pandas to remove duplicate rows based on the email column.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate rows based on the email column, keeping only the first occurrence
    return customers.drop_duplicates(subset = ["email"])


# Example usage
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}

customers = pd.DataFrame(data)
print(customers)

result = dropDuplicateEmails(customers)
print(result)
