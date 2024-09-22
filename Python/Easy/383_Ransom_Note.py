"""

Question: Ransom note


Summary: Given two strings 'ransomNote' and 'magazine', 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise. 
Each letter in magazine can only be used once in ransomNote.


Method: Count the frequency of each letter in both 'ransomNote' and 'magazine'.
Compare the counts to determine if 'ransomNote' can be constructed from 'magazine'.


Time complexity: O(n + m), where n' is the length of 'ransomNote' and 'm' is the length of magazine.
Space complexity: O(1) (since the alphabet size is constant)
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each letter in ransomNote and magazine, 
        # and check if ransomNote can be constructed from magazine
        return Counter(ransomNote) <= Counter(magazine)


# Example usage
result = Solution().canConstruct("a", "b")
print(result)  # Output: false
