"""

Question: Get the size of a dataframe

Summary: Write a function to calculate and display the number of rows and columns of the players DataFrame.

Method: Use the 'shape' attribute in pandas to get the dimensions of the DataFrame. 
Return the dimensions as an array [number of rows, number of columns].

Time complexity: O(1)
Space complexity: O(1)
"""

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # Get the number of rows and columns
    return [players.shape[0], players.shape[1]]


# Example usage
data = {
    'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
    'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
    'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
    'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
    'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
}
players = pd.DataFrame(data)

result = getDataframeSize(players)
print(result)  # Output: [10, 5]
