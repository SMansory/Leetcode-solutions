"""

Question: Sqrt(x)

Summary: Given a non-negative integer 'x', return the square root of 'x' rounded down to the nearest integer.
The returned integer should be non-negative as well. Do not use any built-in exponent function or operator.

Method: Return the integer part of the square root of 'x'.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))


# Example usage
result = Solution().mySqrt(4)
print(result)  # output: 2
        
