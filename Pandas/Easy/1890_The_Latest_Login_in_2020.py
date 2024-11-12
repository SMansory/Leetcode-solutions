"""

Question: The latest login in 2020

Summary: Write a function to report the latest login for all users in the year 2020. 
Do not include the users who did not login in 2020. Return the result table in any order.

Method: Filter the logins to include only those from the year 2020. Rename the 'time_stamp' column to 'last_stamp'. 
Group by 'user_id' and find the maximum 'last_stamp' for each user.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    # Filter logins to include only those from the year 2020 and rename the timestamp column
    filt = logins[logins["time_stamp"].dt.year == 2020].rename(columns = {"time_stamp": "last_stamp"})
    # Group by 'user_id' and find the maximum 'last_stamp' for each user
    return filt.groupby(["user_id"])[["last_stamp"]].max().reset_index()


# Example usage
data = {
    'user_id': [6, 6, 6, 8, 8, 2, 2, 14, 14],
    'time_stamp': pd.to_datetime([
        '2020-06-30 15:06:07', '2021-04-21 14:06:06', '2019-03-07 00:18:15',
        '2020-02-01 05:10:53', '2020-12-30 00:46:50', '2020-01-16 02:49:50',
        '2019-08-25 07:59:08', '2019-07-14 09:00:00', '2021-01-06 11:59:59'
    ])
}
logins = pd.DataFrame(data)

result = latest_login(logins)
print(result)
