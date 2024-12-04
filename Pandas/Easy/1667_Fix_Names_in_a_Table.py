"""

Question: Fix names in a table

Summary: Write a function that transforms the names in a DataFrame so that only the first character is uppercase and 
the rest are lowercase. Sort the final DataFrame by 'user_id'.

Method: Use the 'str.capitalize()' method in pandas to capitalize the first character and 
lowercase the rest for each name in the users DataFrame. Sort the DataFrame by 'user_id'.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Capitalize the first character and lowercase the rest
    users["name"] = users["name"].str.capitalize()
    # Sort the DataFrame by 'user_id'
    return users.sort_values("user_id")


# Example usage
data = {
    'user_id': [1, 2],
    'name': ['aLice', 'bOB']
}
users = pd.DataFrame(data)

result = fix_names(users)
print(result)
