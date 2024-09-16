"""

Question: Find the integer added to array I

Summary: Given two arrays of equal length 'nums1' and 'nums2',
each element in 'nums1' has been increased or decreased by an integer 'x 'such that 'nums1' becomes equal to 'nums2'.
Return the integer 'x'.

Method: Sort both arrays and find the difference between the first elements of the sorted arrays.

Time complexity: O(n log n), where n is the length of the arrays.
Space complexity: O(1)
"""

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        # Sort both arrays
        nums1.sort()
        nums2.sort()

        # Return the differene between the first elements of the sorted arrays
        return nums2[0] - nums1[0]


# Example usage
result = Solution().addedInteger([2, 6, 4], [9, 7, 5])
print(result)  # Output: 3
