"""

Question: Big countries

Summary: Write a function to find the name, population, and area of the big countries.
A country is considered big if it has an area of at least three million km² or a population of at least twenty-five million.
Return the result table in any order.

Method: Use the 'loc' method in pandas to filter the world DataFrame for rows where
the 'area' is at least 3000000 or the population is at least 25000000. 
Select the 'name', 'population', and 'area' columns from the filtered DataFrame.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where 'area' is at least 3000000 or 'population' is at least 25000000
    return world.loc[(world["area"] >= 3000000) | (world["population"] >= 25000000), ["name", "population", "area"]]


# Example usage
data = {
    'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
    'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
    'area': [652230, 28748, 2381741, 468, 1246700],
    'population': [25500100, 2831741, 37100000, 78115, 20609294],
    'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
}
world = pd.DataFrame(data)

result = big_countries(world)
print(result)
