"""

Question: Not boring movies

Summary: Write a function to report the movies with an odd-numbered ID and a description that is not "boring". 
Return the result table ordered by rating in descending order.

Method: Filter the DataFrame to include only rows where 'id' is odd and the 'description' is not "boring". 
Then sort the DataFrame by 'rating' in descending order.

Time complexity: O(n log n)
Space complexity: O(n)
"""

import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where 'id' is odd and 'description' is not "boring" and sort by 'rating' in descending order
    return cinema.loc[(cinema["description"] != "boring") & (cinema["id"] % 2 != 0)].sort_values(by = "rating", ascending = False)


# Example usage
data = {
    'id': [1, 2, 3, 4, 5],
    'movie': ['War', 'Science', 'irish', 'Ice song', 'House card'],
    'description': ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'],
    'rating': [8.9, 8.5, 6.2, 8.6, 9.1]
}
cinema = pd.DataFrame(data)

result = not_boring_movies(cinema)
print(result)
