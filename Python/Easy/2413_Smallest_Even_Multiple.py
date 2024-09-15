"""
Problem: Smallest even multiple

Summary: Given a positive integer 'n', return the smallest positive integer that is a multiple of 2 and 'n'.

Method: Check if 'n is even. If it is, return 'n'; otherwise, return 'n * 2'.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        # Check if 'n' is even
        if n % 2 == 0:
            return n
        else:
            return n * 2


# Example usage
result = Solution().smallestEvenMultiple(5)
print(result)  # Output: 10
