"""
Question: Sum of elements with indices having K set bits

Summary: Given a 0-indexed integer array 'nums' and an integer 'k', 
return the sum of elements in 'nums' whose corresponding indices have exactly 'k' set bits in their binary representation. 
The set bits in an integer are the 1's present when it is written in binary.

Method: Iterate through the array and check the number of set bits in the binary representation of each index. 
Sum the elements whose indices have exactly 'k' set bits.

Time complexity: O(n * log n)
Space complexity: O(1)
"""

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0

        # Iterate through the array
        for i in range(0, n):
            # Check if the number of set bits in the binary representation of 'i' is equal to 'k'
            if str(bin(i)[2:]).count("1") == k:
                result += nums[i]
              
        return result


# Example usage
result = Solution().sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1)
print(result)  # Output: 13
