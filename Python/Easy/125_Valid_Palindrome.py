"""

Question: Valid palindrome

Summary: A string is a palindrome if,
after converting all uppercase letters into lowercase and removing all non-alphanumeric characters,
it reads the same forward and backward. Given a string 's', return true if it is a palindrome, otherwise return false.

Method: Convert the string to lowercase, remove all non-alphanumeric characters,
and check if the resulting string reads the same forward and backward.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = "".join([i for i in s.lower() if i in "1234567890qwertyyuiopasdfghjklzxcvbnm"])
        # Check if the processed string is a palindrome
        return s == s[::-1]


# Example usage
result = Solution().isPalindrome("race a car")
print(result)  # Output: false
