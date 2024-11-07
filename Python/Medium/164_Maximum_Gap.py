"""

Question: Maximum gap

Summary: Given an integer array 'nums', return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0. The solution should run in linear time and use linear extra space.

Method: Sort the array and iterate through it to find the maximum difference between successive elements.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
          
        nums.sort()
        arr = []
      
        for i in range(len(nums) - 1):
            arr.append(nums[i + 1] - nums[i])
          
        return max(arr)


# Example usage
result = Solution().maximumGap([3, 6, 9, 1])
print(result)  # Output: 3
