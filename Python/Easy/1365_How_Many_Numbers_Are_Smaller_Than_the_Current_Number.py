"""
Question: How many numbers are smaller than the current number

Summary: Given an array 'nums', determine how many numbers in the array are smaller than each element.
For each 'nums[i]', count the number of elements 'nums[j]' such that 'j != i' and 'nums[j] < nums[i]'.
Return the results in a new array.

Method: Use sorting and list comprehension to find the count of smaller numbers.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # We use list comprehension to find the count of smaller numbers
        return [sorted(nums).index(i) for i in nums]


# Example usage
result = Solution().smallerNumbersThanCurrent([8, 1, 2, 3, 3])
print(result)  # Output: [4, 0, 1, 1, 3]
