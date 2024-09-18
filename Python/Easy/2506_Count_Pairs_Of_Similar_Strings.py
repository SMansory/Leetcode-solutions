"""

Question: Count pairs of similar strings

Summary: Given a 0-indexed string array 'words', 
return the number of pairs '((i, j))' such that '(0 <= i < j <= words.length - 1)' and 
the two strings 'words[i]' and 'words[j]' are similar. 
Two strings are considered similar if they consist of the same characters.

Method: Use nested loops to compare each pair of strings. 
Convert each string to a set of characters and check if the sets are equal.

Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
      
        for i in range(len(words)):
            for j in range(i):
                # Check if the sets of characters are equal
                if set(words[i]) == set(words[j]):
                    count += 1
                  
        return count


# Example usage
result = Solution().similarPairs(["aba", "aabb", "abcd", "bac", "aabc"])
print(result)  # Output: 2
