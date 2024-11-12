"""

Question: Game play analysis I

Summary: Write a function to find the first login date for each player. Return the result table in any order.

Method: Group the activity DataFrame by 'player_id' and use the 'min' function to find the earliest 'event_date' for each player.
Reset the index and rename the 'event_date' column to 'first_login'.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by 'player_id' and find the earliest 'event_date'
    return activity.groupby("player_id")["event_date"].min().reset_index().rename(columns = {"event_date": "first_login"}) 


# Example usage
data = {
    'player_id': [1, 1, 2, 3, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': pd.to_datetime(['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03']),
    'games_played': [5, 6, 1, 0, 5]
}
activity = pd.DataFrame(data)

result = game_analysis(activity)
print(result)
