"""

Question: Rank scores

Summary: Write a function that ranks the scores from highest to lowest. 
In the event of a tie, both scores share the same rank, 
and the next rank is the next consecutive integer. Return the result ordered by 'score' in descending order.

Method: First, sort the 'scores' DataFrame by the 'score' column in descending order. 
Then, use the 'rank()' method with the dense ranking method to assign ranks.
Finally, return the DataFrame with 'score' and 'rank' columns.

Time complexity: O(n log n) - Sorting the DataFrame.
Space complexity: O(n)
"""

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort the 'scores' in descending order
    df = scores.sort_values(by="score", ascending=False)
    # Assign ranks using the dense ranking method
    df["rank"] = df["score"].rank(method="dense", ascending=False)
    # Return the DataFrame with 'score' and 'rank' columns
    return df[["score", "rank"]]


# Example usage
scores_data = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}
scores = pd.DataFrame(scores_data)

result = order_scores(scores)
print(result)
