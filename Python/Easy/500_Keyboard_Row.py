"""

Question: Keyboard row

Summary: Given an array of strings 'words',
return the words that can be typed using letters from only one row of an American keyboard. The rows are defined as follows:
First row: “qwertyuiop”
Second row: “asdfghjkl”
Third row: “zxcvbnm”

Method: Use sets to represent each row of the keyboard. 
For each word, check if all its characters belong to one of these sets.

Time complexity: O(n * m) (where 'n' is the number of words and 'm' is the average length of the words)
Space complexity: O(n)
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM"
      
        result = []
      
        for word in words:
            # Check if the word can be typed using one row of the keyboard
            if set(word).issubset(row1) or set(word).issubset(row2) or set(word).issubset(row3):
                result.append(word)
              
        return result


# Example usage
result = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
print(result)  # Output: ["Alaska", "Dad"]
