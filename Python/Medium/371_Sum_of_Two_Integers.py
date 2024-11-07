"""

Question: Sum of two integers

Summary: Find the sum of the two integers 'a' and 'b' without using the + and - operators.

Method: Use the built-in 'sum' function to compute the sum of the two integers by passing them as elements of a list.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])


# Example usage
result = Solution().getSum(1, 2)
print(result)  # Output: 3
