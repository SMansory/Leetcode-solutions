"""

Question : Power of three

Summary: Given an integer 'n', return true if it is a power of three, otherwise return false.
An integer 'n' is a power of three if there exists an integer 'x' such that 𝑛 = (3 to the power of 𝑥).

Method: Use recursion to check if the integer can be reduced to 1 by repeatedly dividing by 3.

Time complexity: O(log n)
Space complexity: O(log n) due to recursion stack
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Base case: 'n' is 1, which is 3^0
        if n == 1:
            return True

        # Base case: 'n' is less than 3 and not 1, hence cannot be power of three
        elif n < 3:
            return False

        # Recursive case: check if 'n' divided by 3 is still a power of three
        return self.isPowerOfThree(abs(n) / 3)


# Example usage
result = Solution().isPowerOfThree(27)
print(result)  # Output: true
