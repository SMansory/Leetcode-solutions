"""

Question: Number of changing keys

Summary: Given a 0-indexed string 's' typed by a user, determine the number of times the user had to change the key.
Changing a key is defined as using a key different from the last used key.
Modifiers like shift or caps lock are not counted as key changes.

Method: Convert the string to lowercase to ignore case differences, 
then iterate through the string and count the number of times consecutive characters are different.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        count = 0
      
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                count += 1
              
        return count


# Example usage
result = Solution().countKeyChanges("aAbBcC")
print(result)  # Output: 2
