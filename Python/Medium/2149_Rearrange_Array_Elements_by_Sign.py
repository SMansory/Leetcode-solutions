"""

Question: Rearrange array elements by sign

Summary: Given an array 'nums' of even length with an equal number of positive and negative integers,
return the array such that every consecutive pair of integers has opposite signs, 
preserving the order of integers with the same sign. The rearranged array begins with a positive integer.

Method: Separate the positive and negative integers into two lists, then interleave them to create the rearranged array.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Separate the positive and negative integers
        positive = [i for i in nums if i > 0]
        negative = [i for i in nums if i < 0]
        arr = []

        # Interleave the positive and negative integers
        for i in range(len(nums) // 2):
            arr.append(positive[i])
            arr.append(negative[i])
          
        return arr


# Example usage
result = Solution().rearrangeArray([3, 1, -2, -5, 2, -4])
print(result)  # Output: [3, -2, 1, -5, 2, -4]
