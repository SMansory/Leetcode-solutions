"""

Question: Perform XOR operations in an array

Summary: Given an integer 'n' and an integer 'start', 
define an array 'nums' where 'nums[i] = start + 2 * i' (0-indexed) and 'n == nums.length'.
Return the bitwise XOR of all elements in 'nums'.

Method: Iterate through the array, calculating the XOR of each element with the result.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        # Iterate through the array and perform XOR operations
        for i in range(0, n):
            res ^= start + 2 * i 
          
        return res


# Example usage
result = Solution().xorOperation(5, 0)
print(result)  # Output: 8
