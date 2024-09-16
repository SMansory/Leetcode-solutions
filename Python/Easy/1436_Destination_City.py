"""

Question: Destination city

Summary: Given an array 'paths' where each element 'paths[i] = [cityAi, cityBi]' represents a direct path from 'cityAi' to 'cityBi',
determine the destination city. The destination city is defined as the city that does not have any outgoing paths to another city.
It is guaranteed that the graph forms a line without any loops, ensuring there is exactly one destination city.

Method: Use set operations to find the city that appears only as a destination and not as a starting point.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set(i[1] for i in paths) - set(i[0] for i in paths)).pop()


# Example usage
result = Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
print(result)  # Output: "Sao Paulo"
