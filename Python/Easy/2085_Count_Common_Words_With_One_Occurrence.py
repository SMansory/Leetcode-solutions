"""

Question: Count common words with one occurrence

Summary: Given two string arrays 'words1' and 'words2', return the number of strings that appear once in both arrays.

Method: Iterate through words1 and use the count method to check if each string appears exactly once in both arrays.

Time complexity: O(n * m) (where 'n' is the length of 'words1' and 'm' is the length of 'words2')
Space complexity: O(1)
"""

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0 
      
        for i in words1:
            # Check if the string appears exactly once in both arrays
            if words1.count(i) == 1 and words2.count(i) == 1:
                count += 1
              
        return count


# Example usage
result = Solution().countWords(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"])
print(result)  # Output: 2
