"""

Question: Find xor-beauty of array

Summary: Calculate the XOR beauty of a given 0-indexed integer array 'nums' 
by XORing the effective values of all possible triplets of indices.

Method: Use the reduce function with the 'xor' operator to compute the XOR beauty of the array.

Time complexity: O(n)
Space complexity: O(1)
"""

from functools import reduce 
from operator import xor

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(xor, nums)


# Example usage
result = Solution().xorBeauty([1, 4])
print(result)  # Output: 5
