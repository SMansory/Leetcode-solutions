"""

Question: Valid anagrams

Summary:  You are given two strings 's' and 't', return true if 't' is an anagram of 's', and false otherwise.

Method: Sort both strings and compare them. If they are equal, then 't' is an anagram of 's'.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings and compare them
        return True if sorted(s) == sorted(t) else False


# Example usage
result = Solution().isAnagram("rat", "car")
print(result)  # Output: false
