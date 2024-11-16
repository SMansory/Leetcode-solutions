"""

Question: Find followers count

Summary: Write a function that will, for each user, return the number of followers. 
Return the result table ordered by 'user_id' in ascending order.

Method: Group the followers DataFrame by 'user_id' and count the occurrences of 'follower_id' for each group.
Reset the index and rename the 'follower_id' column to 'followers_count'.
Sort the resulting DataFrame by 'user_id' in ascending order.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
       # Group by 'user_id' and count the occurrences of 'follower_id'
       result = followers.groupby("user_id")["follower_id"].count().reset_index()
       # Rename the column to 'followers_count'
       result.rename(columns = {"follower_id": "followers_count"}, inplace = True)
       # Sort the result by 'user_id' in ascending order
       return result.sort_values(by = "user_id", ascending = True)


# Example usage
data = {
    'user_id': [0, 1, 2, 2],
    'follower_id': [1, 0, 0, 1]
}
followers = pd.DataFrame(data)

result = count_followers(followers)
print(result)
