"""

Question: Hamming distance

Summary: The Hamming distance between two integers is defined as 
the number of positions at which the corresponding bits differ. Given two integers 'x' and 'y',
return the Hamming distance between them.

Method: Use the XOR operation to find differing bits and count the number of 1s in the binary representation of the result.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers and count the number of 1s in the binary representation
        return bin(x ^ y).count("1")


# Example usage
result = Solution().hammingDistance(1, 4)
print(result)  # Output: 2
