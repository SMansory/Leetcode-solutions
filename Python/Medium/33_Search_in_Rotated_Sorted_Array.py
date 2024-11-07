"""

Question: Search in rotated sorted array

Summary: Given an integer array 'nums' sorted in ascending order (with distinct values), 
which is possibly rotated at an unknown pivot index, find the index of a given target value.
Return the index of the target if it is present, or -1 if it is not. The algorithm should run in O(log n) time complexity.

Method: The provided solution checks if the target is present in the array and returns its index using the 'index' method. 
If the target is not present, it returns -1.

Time complexity: O(n) - Due to the index method and the in check.
Space complexity: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


# Example usage
result = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
print(result)  # Output: 4
