"""

Question: Number of strings that appear as substrings in word

Summary: Given an array of strings 'patterns' and a string 'word', 
determine how many strings in 'patterns' appear as substrings within 'word'. 
A substring is a contiguous sequence of characters within a string.

Method: Loop through each string in the 'patterns' array and check if it is a substring of 'word'. 
Count the number of such occurrences.

Time complexity: O(n * m), where n is the number of 'patterns' and m is the length of the 'word'.
Space complexity: O(1)
"""

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
      
        for i in patterns:
            if i in word:
                count += 1
              
        return count


# Example usage
result = Solution().numOfStrings(["a", "abc", "bc", "d"], "abc")
print(result)  # Output: 3
