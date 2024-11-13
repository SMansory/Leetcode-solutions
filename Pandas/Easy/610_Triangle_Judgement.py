"""

Question: Triangle judgement

Summary: Write a function to report for every three line segments whether they can form a triangle. 
Return the result table in any order.

Method: Check if the sum of any two sides is greater than the third side for each set of three line segments.
If this condition is true for all three combinations, the segments can form a triangle.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    # Check if the sum of any two sides is greater than the third side
    triangle["triangle"] = (triangle["x"] + triangle["y"] > triangle["z"]) & (triangle["x"] + triangle["z"] > triangle["y"]) & (triangle["y"] + triangle["z"] > triangle["x"])
    # Apply the condition and label as "Yes" or "No"
    triangle["triangle"] = triangle["triangle"].apply(lambda x: "Yes" if x else "No")
    return triangle


# Example usage
data = {
    'x': [13, 10],
    'y': [15, 20],
    'z': [30, 15]
}
triangle = pd.DataFrame(data)

result = triangle_judgement(triangle)
print(result)
