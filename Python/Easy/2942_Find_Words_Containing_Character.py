"""
Problem: Find words containing character
Summary: Given a 0-indexed array of strings 'words' and a character 'x', return an array of indices representing the words that contain the character 'x'.
The returned array may be in any order.
Method: List comprehension with enumeration to find indices of words containing the character.
Time Complexity: O(n * m), where n is the number of words and m is the average length of the words.
Space Complexity: O(n)
"""

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Use list comprehension with enumeration to find indices of words containing the character.
        indices_list = [index for index, char in enumerate(words) if x in char]
      
        return indices_list


# Example usage
result = Solution().findWordsContaining(["leet","code"], "e")
print(result)  # Output:  [0,1]
