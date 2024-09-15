"""
Problem: Sum of two integers
Summary: Given two integers 'num1' and 'num2', return their sum.
Method: Simple addition of the two integers.
Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        # Calculate the sum of num1 and num2 
        sum = num1 + num2
        return sum


# Example usage
result = Solution().sum(4, -10)
print(result)  # Output: -6
