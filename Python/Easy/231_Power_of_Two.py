"""

Question: Power of two

Summary: Given an integer 'n', return true if it is a power of two, otherwise return false.
An integer 'n' is a power of two if there exists an integer 'x' such that 𝑛 = (2 to the power of 𝑥).

Method: Use a bitwise operation to check if 'n' is a power of two.
If 'n' is non-zero and the bitwise AND of 'n' and n - 1 equals zero, then 'n' is a power of two.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if 'n' is non-zero and 'n' & (n - 1) is zero
        if (n != 0) and ((n & (n - 1)) == 0):
            return True


# Example usage
result = Solution().isPowerOfTwo(1)
print(result)  # Output: true
