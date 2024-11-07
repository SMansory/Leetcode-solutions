"""

Question: Find first and last position of element in sorted array

Summary: Given an array of integers 'nums' with non-decreasing order,
find the starting and ending position of a given target value. If the target is not in the array, return [-1, -1]. 
The solution must run in O(log n) runtime complexity.

Method: Iterate through the array to find the indices of the target value, store them in a list,
and return the first and last index of the target value from the list. If the target value is not found, return [-1, -1].

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        my_list = []
      
        if not(target in nums):
            return [-1, -1]
          
        for i in range(len(nums)):
            if nums[i] == target:
                my_list.append(i)
              
        return [my_list[0], my_list[-1]]


# Example usage
result = Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
print(result)  # Output: [3, 4]
