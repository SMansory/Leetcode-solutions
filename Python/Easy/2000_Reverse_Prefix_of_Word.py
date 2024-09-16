"""

Question: Reverse the prefix of a string up to a given character

Summary: Given a 0-indexed string word and 'a' character 'ch',
reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of 'ch' (inclusive).
If 'ch' does not exist in word, return the string unchanged.

Method: Iterate through the string to find the first occurrence of 'ch'. 
Reverse the substring from the start to this index and concatenate it with the remainder of the string.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = ""
        # Iterate through the string to find the first occurence of the 'ch'
        for i in range(len(word)):
            if word[i] == ch:
                ans = word[:i+1]
                result = ans[::-1]
                break
        # Concatenate the reversed prefix with the remainder of the string 
        return result + word[len(result):]


# Example usage
result = Solution().reversePrefix("abcdefd", "d")  
print(result)  # Output: "dcbaefd"
