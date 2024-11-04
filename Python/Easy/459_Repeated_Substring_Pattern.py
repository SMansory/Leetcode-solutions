"""

Question: Repeated substring pattern

Summary: You are given a string 's', 
determine if it can be constructed by taking a substring and appending multiple copies of it together.

Method: Concatenate the string 's' with itself, then check if 's' exists within this new string, 
excluding the first and last characters.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1 = s + s
        return s in s1[1:-1]


# Example usage
result = Solution().repeatedSubstringPattern("aba")
print(result)  # Output: false
