"""

Question: Number of 1 bits

Summary: Write a function that takes a positive integer and returns the number of set bits (1s) in its binary representation.
This is also known as the Hamming weight.

Method: Convert the integer to its binary representation and count the number of 1s.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert the integer to binary and count the number of 1s
        return bin(n).count("1")


# Example usage
result = Solution().hammingWeight(11)
print(result)  # Output: 3
