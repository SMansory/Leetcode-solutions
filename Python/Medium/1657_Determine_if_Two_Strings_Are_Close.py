"""

Question: Determine if two strings are close

Summary: Determine if two strings, 'word1' and 'word2', are close by using the allowed operations: 
swapping any two characters and transforming every occurrence of one character into another.

Method: Check if the lengths of the two strings are the same and if they contain the same unique characters.
Then, count the frequency of each character in both strings, sort these frequencies, and compare them.

Time complexity: O(n log n)
Space complexity: O(n)
"""

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        list1 = [v for k, v in Counter(word1).items()]
        list2 = [v for k, v in Counter(word2).items()]
    
        list1.sort()
        list2.sort()
  
        return list1 == list2


# Example usage
result = Solution().closeStrings("abc", "bca")
print(result)  # Output: true
