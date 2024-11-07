"""

Question: Median of two sorted arrays

Summary: Return the median of the combined sorted arrays 'nums1' of size 'm' and 'nums2' of size 'n'. 
The overall runtime complexity should be O(log (m+n)).

Method: Combine the two arrays, sort the combined array, and use the median function to find the median value.

Time complexity: O((m + n) log (m + n)) - Combining and sorting the arrays.
Space complexity: O(m + n) - Storing the combined array.
"""

from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))


# Example usage
result = Solution().findMedianSortedArrays([1, 3], [2])
print(result)  # Output: 2.00000
