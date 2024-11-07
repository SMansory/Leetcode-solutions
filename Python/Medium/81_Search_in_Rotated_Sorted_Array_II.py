"""

Question: Search in rotated sorted array II

Summary: Given a non-decreasing order integer array 'nums' that has been rotated at an unknown pivot index,
determine if a target value exists in the array. The goal is to minimize the number of operations.

Method: Use the 'in' keyword to check if the target is present in the array.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums


# Example usage
result = Solution().search([2, 5, 6, 0, 0, 1, 2], 0)
print(result)  # Output: true
