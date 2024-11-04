"""

Question: Largest number at least twice of others

Summary: Given an integer array 'nums', where the largest integer is unique, 
determine if the largest element is at least twice as much as every other number in the array.
If true, return the index of the largest element; otherwise, return -1.

Method: Find the maximum element in the array. Check if this element is at least twice every other element.
If the condition holds, return the index of the maximum element; otherwise, return -1.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxi = max(nums)

        for i in nums:
            if maxi < 2*i and i != maxi:
                return -1

        return nums.index(maxi)


# Example usage
result = Solution().dominantIndex([3, 6, 1, 0])
print(result)  # Output: 1
