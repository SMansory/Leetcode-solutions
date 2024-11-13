"""

Question: Duplicate emails

Summary: Write a function to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
Return the result table in any order.

Method: Use the 'duplicated' method in pandas to identify duplicate emails.
Select the 'email' column and remove any further duplicates to ensure each email is listed only once.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # Identify duplicate emails and select the 'email' column
    result = person.loc[person.duplicated(subset = ["email"]), ["email"]]
    # Remove any further duplicates
    return result.drop_duplicates()


# Example usage
data = {
    'id': [1, 2, 3],
    'email': ['a@b.com', 'c@d.com', 'a@b.com']
}
person = pd.DataFrame(data)

result = duplicate_emails(person)
print(result)
