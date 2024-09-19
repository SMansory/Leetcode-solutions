"""

Question: Minimum string length after removing substrings

Summary: Given a string 's' consisting only of uppercase English letters,
you can repeatedly remove any occurrence of the substrings “AB” or “CD”. 
Return the minimum possible length of the resulting string.
Note that removing a substring may create new occurrences of “AB” or “CD”.

Method: Use a loop to iteratively remove “AB” or “CD” substrings until none are left.

Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def minLength(self, s: str) -> int:
        for i in range(len(s)):
            if "AB" in s:
                s = s.replace("AB", "")
            elif "CD" in s:
                s = s.replace("CD", "") 
              
        return len(s)


# Example usage
result = Solution().minLength("ABFCACDB")
print(result)  # Output: 2
