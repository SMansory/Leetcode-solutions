"""

Question: Length of last word

Summary: Given a string 's' that contains words and spaces, return the length of the last word in the string. 
A word is a maximal substring consisting of non-space characters only.

Method: Remove any trailing spaces from the string, split the string into words, and return the length of the last word.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.strip()
        ans1 = ans.split(" ")
        return len(ans1[-1])


# Example usage
result = Solution().lengthOfLastWord("Hello World")
print(result)  # Output: 5
