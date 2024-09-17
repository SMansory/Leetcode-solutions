"""

Question: Special array I

Summary: An array is considered special if every pair of its adjacent elements has different parity 
(one is even, the other is odd). Given an array of integers 'nums', return true if the array is special,
otherwise return false.

Method: Iterate through the array and check if the sum of each pair of adjacent elements is odd. 
If any pair has the same parity, return false.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            # Check if the sum of adjacent elements is even
            if (nums[i - 1] + nums[i]) % 2 == 0:
                return False
        return True


# Example usage
result = Solution().isArraySpecial([1])
print(result)  # Output: true
