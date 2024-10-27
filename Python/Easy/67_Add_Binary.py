"""

Question: Add binary

Summary: Given two binary strings, return their sum as a binary string.

Method: Convert the binary strings to integers, sum them, and convert the result back to a binary string.

Time complexity: O(n) 
Space complexity: O(1)
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


result = Solution().addBinary("11", "1")
print(result)  # Output: "100"
