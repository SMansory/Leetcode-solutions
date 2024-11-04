"""

Question: Isomorphic strings

Summary: Given two strings 's' and 't', return true if they are isomorphic.
Two strings are isomorphic if the characters in 's' can be replaced to get 't', while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Method: Use sets to check if the zipped pairs of characters in 's' and 't' 
have the same length as the sets of unique characters in 's' and 't'.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


# Example usage
result = Solution().isIsomorphic("egg", "add")
print(result)  # Output: true
