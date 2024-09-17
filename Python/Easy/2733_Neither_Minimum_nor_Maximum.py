"""

Question: Neither minimum nor maximum

Summary: Given an array of distinct positive integers 'nums', 
find and return any number from the array that is neither the smallest nor the largest value. 
If no such number exists, return -1.

Method: Sort the array and return the second element if the array has at least three elements. Otherwise, return -1.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        return -1 if len(nums) < 3 else nums[1]


# Example usage
result = Solution().findNonMinOrMax([3, 2, 1, 4])
print(result)  # Output: 2
