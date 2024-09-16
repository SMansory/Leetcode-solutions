"""

Question: Sort the people

Summary: Given an array of strings 'names' and an array of distinct positive integers 'heights', both of length 'n', 
return the 'names' sorted in descending order by the corresponding 'heights'.

Method: Use the zip function to pair each name with its corresponding height, 
sort these pairs in descending order by height, and then extract the names from the sorted pairs.

Time complexity: O(n log n)
Space complexity: O(n)
"""


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair each name with its corresponding height and sort it in descending order by height
        return[name for _, name in sorted(zip(heights, names), reverse = True)]


# Example usage
result = Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
print(result)  # Output: ["Mary", "Emma", "John"]
