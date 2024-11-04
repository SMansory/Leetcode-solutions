"""

Question: Find the index of the first occurrence in a string

Summary: You are given two strings 'needle' and 'haystack',
return the index of the first occurrence of 'needle' in 'haystack', or -1 if 'needle' is not part of 'haystack'.

Method: Use the built-in 'find' method of the string class to find the index of the first occurrence of 'needle' in 'haystack'.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# Example usage
result = Solution().strStr("sadbutsad", "sad")
print(result)  # Output: 0
