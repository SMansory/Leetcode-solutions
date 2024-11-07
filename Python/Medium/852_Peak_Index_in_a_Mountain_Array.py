"""

Question: Peak index in a mountain array

Summary: Given a mountain array where values increase to a peak element and then decrease, find the index of the peak element.

Method: Use the 'index' method to find the index of the maximum element in the array, which corresponds to the peak.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


# Example usage
result = Solution().peakIndexInMountainArray([0, 1, 0])
print(result)  # Output: 1
