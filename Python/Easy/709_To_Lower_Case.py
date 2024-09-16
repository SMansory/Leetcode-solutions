"""

Question: To lower case

Summary: Given a string 's', return the string after converting every uppercase letter to its corresponding lowercase letter.

Method: Use the built-in lower() method to convert all uppercase letters in the string to lowercase.

Time complexity: O(n), where n is the length of the string.
Space complexity: O(n)
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        # Convert all uppercase letters to lowercase
        lower = s.lower()
        return lower


# Example usage
result = Solution().toLowerCase("Hello")
print(result)  # Output: "hello"
