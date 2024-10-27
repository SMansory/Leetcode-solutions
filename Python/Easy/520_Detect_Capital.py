"""
Question: Detect capital

Summary: Given a string 'word', return true if one of the following cases holds:
1. All the letters in the string are capitals.
2. All the letters in the string are not capitals.
3. Only the first letter in the string is capital and the rest are not capitals.

Method: Check if the word is entirely in uppercase, entirely in lowercase, or if only the first letter is capitalized.

Time complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if (word == word.upper()) or (word == word.lower()) or (word == word.capitalize()):
            return True
        return False


# Example usage
result = Solution().detectCapitalUse("USA")
print(result)  # Output: true
