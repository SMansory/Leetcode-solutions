"""

Question: Method chaining

Summary: Write a function to list the names of animals that weigh strictly more than 100 kilograms. 
Return the animals sorted by weight in descending order.

Method: Filter the DataFrame to include only rows where 'weight' is greater than 100.
Sort the resulting DataFrame by 'weight' in descending order and select the 'name' column.

Time complexity: O(n log n) 
Space complexity: O(n)
"""

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where 'weight' is greater than 100, sort by 'weight' in descending order and select the 'name' column
    return animals[animals["weight"] > 100].sort_values("weight", ascending = False)[["name"]]


# Example usage
data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}
animals = pd.DataFrame(data)

result = findHeavyAnimals(animals)
print(result)
