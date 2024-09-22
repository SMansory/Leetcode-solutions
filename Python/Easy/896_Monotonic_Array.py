"""

Question: Monotonic Array


Summary: An array is considered monotonic if it is either entirely non-increasing or non-decreasing. 
Given an integer array 'nums', return true if the array is monotonic, otherwise return false.


Method: Compare the array with its sorted version and its reverse sorted version to check for monotonicity.


Time complexity: O(n log n) due to sorting
Space complexity: O(n) for storing the sorted arrays
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Check if the array is either sorted in ascending or descending order
        return nums == sorted(nums) or nums == sorted(nums)[::-1]


# Example usage
result = Solution().isMonotonic([1, 2, 2, 3])
print(result)  # Output: true
