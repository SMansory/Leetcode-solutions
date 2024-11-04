"""

Question: Word pattern

Summary: Given a pattern and a string 's', determine if 's' follows the same pattern. 
This means there must be a one-to-one mapping between each letter in the pattern and each non-empty word in 's'.

Method:
1. Split the string 's' into a list of words.
2. Check if the length of the list of words matches the length of the pattern.
3. Use the zip function to create pairs of words and pattern characters.
4. Use sets to ensure there is a one-to-one mapping between the words and the pattern characters.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
      
        if len(lst) == len(pattern):
            return len(set(zip(lst, list(pattern)))) == len(set(pattern)) == len(set(lst))
          
        return False


# Example usage
result = Solution().wordPattern("abba", "dog cat cat dog")
print(result)  # Output: true
