"""

Question: Palindrome number

Summary: Given an integer 'x', return true if 'x' is a palindrome, and false if it's not.

Method: Convert the integer to a string and check if it reads the same forwards and backwards.

Time Complexity: O(n) (where 'n' is the number of digits in 'x')
Space Complexity: O(n) (due to the string conversion and slicing)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return (True if str(x) == (str(x)[::-1]) else False)


# Example usage
result = Solution().isPalindrome(121)
print(result)  # Output: true
