"""

Question: Valid word

Summary: Determine if a string is a valid word. A valid word contains at least 3 characters, 
only digits and English letters, at least one vowel, and at least one consonant.

Method: Check if the string length is less than 3 and return false. 
Iterate through each character to check if it's alphanumeric, at least one vowel, and at least one consonant. 
Return true if all conditions are met.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def isValid(self, word: str) -> bool:
        x, y = False, False
      
        if len(word) < 3:
            return False
          
        for char in word:
          
            if not char.isalnum():
                return False
            elif char in "aeiouAEIOU":
                x = True
            elif not char.isnumeric():
                y = True

        return x and y


# Example usage
result = Solution().isValid("b3")
print(result)  # Output: false
