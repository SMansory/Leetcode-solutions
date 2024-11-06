"""

Question: Find occurrences of an element in an array

Summary: Given an integer array 'nums', an integer array 'queries', and an integer 'x', 
find the index of the queries[i]th occurrence of 'x' in the 'nums' array for each queries[i]. 
If there are fewer than queries[i] occurrences of 'x', return -1 for that query.

Method: Use a list comprehension to gather the indices of occurrences of 'x' in 'nums'. 
Then, for each query, return the appropriate index or -1 if there are fewer occurrences than requested.

Time complexity: O(n + q) - where 'n' is the length of nums and 'q' is the length of queries.
Space complexity: O(n) - for storing the indices of occurrences.
"""

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        arr = [i for i, num in enumerate(nums) if num == x]
        return [arr[i - 1] if i <= len(arr) else -1 for i in queries]


# Example usage
result = Solution().occurrencesOfElement([1, 3, 1, 7], [1, 3, 2, 4], 1)
print(result)  # Output: [0, -1, 2, -1]
