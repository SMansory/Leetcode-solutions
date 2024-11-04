"""

Question: Power of four

Summary: You are given an integer 'n', return true if it is a power of four, otherwise return false.
An integer 'n' is a power of four if there exists an integer 'x' such that n = (4 to the power of x).

Method: Use recursion to check if the integer can be reduced to 1 by repeatedly dividing by 4.

Time complexity: O(log n)
Space complexity: O(log n) due to recursion stack
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Base case: 'n' is 1, which is 4^0
        if n == 1:
            return True

        # Base case: 'n' is less than 4 and not 1, hence cannot be power of four
        elif n < 4:
            return False

        # Recursive case: check if 'n' divided by 4 is still a power of four
        return self.isPowerOfFour(abs(n) / 4)


# Example usage
result = Solution().isPowerOfFour(16)
print(result)  # Output: true
