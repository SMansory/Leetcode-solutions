"""

Question: Find the encrypted string

Summary: Given a string 's' and an integer 'k',
encrypt the string by replacing each character 'c' with the kth character after 'c' in the string, in a cyclic manner. 
Return the encrypted string.

Method: Use modular arithmetic to determine the new position of each character after shifting by 'k' positions.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        chars = list(s)
      
        for i in range(len(s)):
            # Replace each character with the kth character after it in a cyclic manner
            chars[i] = s[(i + k) % len(s)]
          
        return "".join(chars)


# Example usage
result = Solution().getEncryptedString("dart", 3)
print(result)  # Output: "tdar"
