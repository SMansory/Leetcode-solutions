"""

Question: Minimize string length 

Summary: Given a string 's', you can perform two types of operations:
1. Choose an index 'i' and delete the closest occurrence of the character 'c' at position 'i' to the left of 'i'
(if it exists).
2. Choose an index 'i' and delete the closest occurrence of the character 'c' at position 'i' to the right of 'i' 
(if it exists).
Your task is to minimize the length of 's' by performing these operations zero or more times. 
Return the length of the minimized string.

Method: Convert the string to a set to remove duplicate characters, then return the length of the set.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s = set(s)
        return len(s)


# Example usage
result = Solution().minimizedStringLength("aaabc")
print(result)  # Output: 3
