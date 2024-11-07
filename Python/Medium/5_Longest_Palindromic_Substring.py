"""

Question: Longest palindromic substring

Summary: Given a string 's', identify and return the longest substring that reads the same forward and backward 
(i.e., the longest palindromic substring).

Method: Generate all possible substrings, check if they are palindromes, and return the longest one.

Time complexity: O(n^3) - Generating all substrings and checking if they are palindromes.
Space complexity: O(n^2) - Storing the substrings.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        subStrs = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i: j] == s[i: j][::-1]]
        return max(subStrs, key=len)


# Example usage
result = Solution().longestPalindrome("babad")
print(result)  # Output: "bab"
