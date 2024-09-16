"""
Question: Running sum of an array

Summary: Given an array 'nums', return an array 'runningSum' where 'runningSum[i]' is the sum of elements from 'nums[0]' to 'nums[i]'.

Method: Use list comprehension to calculate the running sum for each index.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # We use list comprehension to calculate the running sum for each index
        return [sum(nums[:i+1]) for i in range(len(nums))]


# Example usage
result = Solution().runningSum([1, 2, 3, 4])
print(result)  # Output: [1, 3, 6, 10]
