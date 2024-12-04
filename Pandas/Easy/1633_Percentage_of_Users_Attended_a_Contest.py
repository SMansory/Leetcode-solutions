"""

Question: Percentage of users attended a contest

Summary: Write a function that calculates the percentage of users registered in each contest, rounded to two decimals.
The final table should be ordered by percentage in descending order, with 'contest_id' used as a tiebreaker in ascending order.

Method: Merge the 'users' DataFrame with the 'register' DataFrame on 'user_id'. 
Group the merged table by 'contest_id' and count the number of users.
Calculate the percentage of users for each contest and sort the final table by 'percentage' in descending order and
'contest_id' in ascending order.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    # Merge the 'users' and 'register' DataFrames on 'user_id'
    merged_table = users.merge(register, on = "user_id")
    # Group by 'contest_id' and count the number of users
    contest = merged_table.groupby(["contest_id"]).agg({"user_id": "count"}).reset_index()
    # Calculate the percentage of users and round to two decimals
    contest["percentage"] = (contest["user_id"] / len(users) * 100).round(2)
    # Sort by 'percentage' in descending order and 'contest_id' in ascending order
    return contest.sort_values(["percentage", "contest_id"], ascending = [False, True])[["contest_id", "percentage"]]


# Example usage
users_data = {
    'user_id': [6, 2, 7],
    'user_name': ['Alice', 'Bob', 'Alex']
}
register_data = {
    'contest_id': [215, 209, 208, 210, 208, 209, 209, 215, 208, 210, 207, 210],
    'user_id': [6, 2, 2, 6, 6, 7, 6, 7, 7, 2, 2, 7]
}

users = pd.DataFrame(users_data)
register = pd.DataFrame(register_data)

result = users_percentage(users, register)
print(result)
