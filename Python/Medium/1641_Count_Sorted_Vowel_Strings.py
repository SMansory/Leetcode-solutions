"""

Question: Count sorted vowel strings

Summary: Determine the number of lexicographically sorted strings 
of a given length 'n' that can be formed using only the vowels (a, e, i, o, u).

Method: Use combinatorial mathematics to calculate the number of lexicographically sorted strings of length 'n' 
consisting only of vowels.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


# Example usage
result = Solution().countVowelStrings(1)
print(result)  # Output: 5
