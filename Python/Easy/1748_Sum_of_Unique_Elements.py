"""

Question: Sum of unique elements

Summary: Given an integer array 'nums', return the sum of all elements that appear exactly once in the array.

Method: Use a list comprehension to iterate through the array and sum up the elements that appear exactly once.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([i for i in nums if nums.count(i) == 1])


# Example usage
result = Solution().sumOfUnique([1, 2, 3, 2])
print(result)  # Output: 4
