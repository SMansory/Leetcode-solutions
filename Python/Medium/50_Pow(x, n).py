"""

Question: Pow(x, n)

Summary: Implement a function to calculate 'x' raised to the power of 'n'.

Method: Use the ** operator to compute the power.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


# Example usage
result = Solution().myPow(2.00000, 10)
print(result)  # Output: 1024.00000
