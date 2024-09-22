"""

Question: Count the number of special characters I

Summary: Given a string 'word', a letter is considered special if it appears both in lowercase and uppercase in the string.
Return the number of special letters in the string.

Method: Iterate through the string, checking if each letter appears in both lowercase and uppercase forms. 
Use a set to store unique special letters and return the size of the set.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = set()
      
        for i in word:
            # Check if the letter appears in both lowercase and uppercase forms
            if (i.lower() in word) and (i.upper() in word):
                result.add(i.lower())

        # Return the number of unique special letters
        return len(result)


# Example usage
result = Solution().numberOfSpecialChars("aaAbcBC")
print(result)  # Output: 3
