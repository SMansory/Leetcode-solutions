"""

Question: Optimal partition of string

Summary: Given a string 's', 
partition the string into the minimum number of substrings such that each substring contains unique characters.
No letter should appear more than once in a single substring.

Method: Iterate through the string, keeping track of characters in the current substring. 
If a character is encountered that is already in the current substring, start a new substring. 
Increment the count of substrings each time a new one is started.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def partitionString(self, s: str) -> int:
        result = 0
        string = ""
      
        for i in s:
            if i in string:
                string = "" + i
                result += 1
            else:
                string += i
              
        return result + 1


# Example usage
result = Solution().partitionString("abacaba")
print(result)  # Output: 4
