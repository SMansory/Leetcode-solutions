"""

Question: Friend requests II: who has the most friends

Summary: Write a function that identifies the person with the most friends and the number of friends they have.
The solution should handle cases where only one person has the most friends.

Method: Combine the 'accepter_id' and 'requester_id' columns into a single list.
Find the person who appears the most in this combined list.
Count the occurrences of this person to determine the number of friends. 
Return the result as a DataFrame with the person's ID and their friend count.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def most_friends(ra: pd.DataFrame) -> pd.DataFrame:
    # Combine accepter_id and requester_id into a single list
    result = list(ra['accepter_id']) + list(ra['requester_id'])
    # Find the person with the most friends
    maxi = max(result, key=result.count)
    # Count the number of friends
    return pd.DataFrame({'id':[maxi], 'num':[result.count(maxi)]})


# Example usage
request_accepted_data = {
    'requester_id': [1, 1, 2, 3],
    'accepter_id': [2, 3, 3, 4],
    'accept_date': ['2016/06/03', '2016/06/08', '2016/06/08', '2016/06/09']
}
ra = pd.DataFrame(request_accepted_data)

result = most_friends(ra)
print(result)
