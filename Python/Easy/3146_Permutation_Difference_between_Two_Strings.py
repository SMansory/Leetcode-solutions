"""
Problem: Permutation difference
Summary: Given two strings 's' and 't' where each character appears at most once in 's' and 't' is a permutation of 's', calculate the permutation difference.
The permutation difference is the sum of the absolute differences between the indices of each character in 's' and the indices of the same characters in 't'.
Method: Iterate through the characters of 't' and calculate the absolute differences between their indices in 's' and 't'.
Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        count = 0
      
        for i in range(len(s)):
            count += abs(s.index(t[i]) - i)
          
        return count


# Example usage
result = Solution().findPermutationDifference("abc", "bac")
print(result)  # Output: 2
