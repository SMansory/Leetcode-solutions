"""

Question: Find Target Indices After Sorting Array

Summary: Given a 0-indexed integer array 'nums' and a target element 'target', 
return a list of indices where 'nums[i]' equals 'target' after sorting 'nums' in non-decreasing order. 
If there are no such indices, return an empty list. The returned list must be sorted in increasing order.

Method: Sort the array and use a list comprehension to find the indices of the target element.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]


# Example usage
result = Solution().targetIndices([1, 2, 5, 2, 3], 2)
print(result)  # Output: [1, 2]
