"""

Question: Find unique character in a string


Summary: You are given a string 's', find the first non-repeating character in it and return its index. 
If it does not exist, return -1.


Method: Use a Counter from the collections module to count the frequency of each character.
Iterate through the string to find the first character with a count of one and return its index.


Time complexity: O(n)
Space complexity: O(n)
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count the frequency of each character in the string
        count = Counter(s)

        # Iterate through the string to find the first non-repeating character
        for index, char in enumerate(s):
            if count[char] == 1:
                return index

        # If no non-repeating character is found, return -1
        return -1


# Example usage
result = Solution().firstUniqChar("leetcode")
print(result)  # Output: 0
