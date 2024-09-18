"""

Question: First letter to appear twice

Summary: Given a string 's' consisting of lowercase English letters, return the first letter that appears two times. 
A letter 'a' appears two times before another letter 'b' if the second occurrence of 'a' is before the second occurrence of 'b'. 
The string 's' will contain at least one letter that appears two times.

Method: Use a dictionary to track the indices of letters as you iterate through the string. 
Return the first letter that appears two times.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letter_indices = {}
        
        for i, letter in enumerate(s):
            # Check if the letter has already been seen
            if letter in letter_indices:
                return letter
            else:
                # Store the index of the letter
                letter_indices[letter] = i
              
        return None


# Example usage
result = Solution().repeatedCharacter("abccbaacz")
print(result)  # Output: "c"
