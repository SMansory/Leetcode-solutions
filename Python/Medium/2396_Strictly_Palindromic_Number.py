"""

Question: Strictly palindromic number

Summary: Given an integer 'n', return true if 'n' is strictly palindromic and false otherwise.
An integer 'n' is strictly palindromic if, for every base 'b' between 2 and n - 2 (inclusive), 
the string representation of 'n' in base 'b' is palindromic. A string is palindromic if it reads the same forward and backward.

Method: Check if the binary representation of 'n' is the same when reversed.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # Convert the integer 'n' to its binary representation
        ans = bin(n)
        # Reverse the binary string
        ans1 = ans[::-1]

        # Check if the binary string is the same when reversed
        if ans == ans1:
            return True
        else:
            return False


# Example usage
result = Solution().isStrictlyPalindromic(9)
print(result)  # Output: false
