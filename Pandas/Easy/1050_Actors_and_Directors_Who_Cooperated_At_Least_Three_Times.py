"""

Question: Actors and directors who cooperated at least three times

Summary: Write a function to find all the pairs ('actor_id', 'director_id') 
where the actor has cooperated with the director at least three times. Return the result table in any order.

Method: Group the 'actor_director' DataFrame by 'actor_id' and 'director_id' and count the occurrences of each pair.
Filter the pairs to include only those where the count is at least 3.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by 'actor_id' and 'director_id' and count the occurrences
    result = actor_director.groupby(["actor_id", "director_id"])["timestamp"].count().reset_index()
    # Filter pairs with at least three occurrences
    return result[result["timestamp"] >= 3][["actor_id", "director_id"]]


# Example usage
data = {
    'actor_id': [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp': [0, 1, 2, 3, 4, 5, 6]
}
actor_director = pd.DataFrame(data)

result = actors_and_directors(actor_director)
print(result)
