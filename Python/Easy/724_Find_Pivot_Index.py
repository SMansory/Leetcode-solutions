"""

Question: Find pivot index


Summary: Given an array of integers 'nums', 
find the pivot index where the sum of the elements to the left of the index is equal to the sum of the elements to the right.
If no such index exists, return -1. 
The pivot index at the edges of the array considers the sum of non-existent elements as 0.


Method: Calculate the total sum of the array. 
Iterate through the array while maintaining the sum of elements to the left of the current index. 
For each index, compute the right sum and compare it with the left sum to find the pivot index.


Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if right == left:
                return i
            
            left += nums[i]
        
        return -1


# Example usage
result = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
print(result)  # Output: 3
