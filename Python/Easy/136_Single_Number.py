"""

Question: Single number

Summary: Given a non-empty array of integers 'nums', where every element appears twice except for one, 
find the single unique element. The solution must have a linear runtime complexity and use only constant extra space.

Method: Iterate through the array and use the count method to find the element that appears only once.

Time complexity: O(n^2) (due to the count method being called inside a loop)
Space complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            # Check if the current element appears only once
            if nums.count(i) == 1:
                return i


# Example usage
result = Solution().singleNumber([2, 2, 1])
print(result)  # Output: 1
