"""

Question: User activity for the past 30 days I

Summary: Write a function that calculates the daily active user count for a 30-day period ending on 2019-07-27.
A user is considered active on a given day if they made at least one activity on that day. 
The result table can be returned in any order.

Method: Filter the 'activity' DataFrame to include only the activities within the specified date range. 
Group by 'activity_date' and count the unique users for each day. 
Rename the columns to match the required output and return the result.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    # Filter activities within the specified date range,
    # Group by 'activity_date' and count unique user IDs,
    # Rename columns to match the required output
    return (
        activity[activity["activity_date"].between("2019-06-28", "2019-07-27")]
        .groupby(by = "activity_date")
        .nunique()
        .reset_index()[["activity_date", "user_id"]]
        .rename(columns = {"activity_date": "day", "user_id": "active_users"})
    )


# Example usage
activity_data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    'session_id': [1, 1, 1, 4, 4, 4, 2, 2, 2, 3, 3],
    'activity_date': ['2019-07-20', '2019-07-20', '2019-07-20', '2019-07-20', '2019-07-21', '2019-07-21', '2019-07-21', '2019-07-21', '2019-07-21', '2019-06-25', '2019-06-25'],
    'activity_type': ['open_session', 'scroll_down', 'end_session', 'open_session', 'send_message', 'end_session', 'open_session', 'send_message', 'end_session', 'open_session', 'end_session']
}
activity = pd.DataFrame(activity_data)

result = user_activity(activity)
print(result)
