"""

Question: Reverse bits


Summary: Given a 32-bit unsigned integer, reverse its bits and return the resulting integer.


Method: Convert the integer to a 32-bit binary string, reverse the string, and then convert it back to an integer.


Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert the integer to a 32-bit binary string
        ans = "{:032b}".format(n)
        # Reverse the binary string
        result = ans[::-1] 
        # Convert the reversed binary string back to an integer
        return int(result, 2)


# Example usage
result = Solution().reverseBits(11111111111111111111111111111101)
print(result)  # Output:    3221225471 (10111111111111111111111111111111)
        
