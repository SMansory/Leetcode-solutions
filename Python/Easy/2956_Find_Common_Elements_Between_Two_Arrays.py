"""

Question: Find common elements between two arrays

Summary: Given two integer arrays 'nums1' and 'nums2', return the number of indices 'i' such that 'nums1[i]' exists in 'nums2' and 
the number of indices 'i' such that 'nums2[i]' exists in 'nums1'.

Method: Iterate through each array and count how many elements from one array exist in the other.

Time complexity: O(n * m), where n is the length of 'nums1' and m is the length of 'nums2'.
Space complexity: O(1)
"""

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = 0, 0

        # Count elements in 'nums1' tht exists in 'nums2'
        for i in nums1:
            if i in nums2:
                a += 1
        # Count elements in 'nums2' tht exists in 'nums1'
        for j in nums2:
            if j in nums1:
                b += 1

        return [a, b]


# Example usage
result = Solution().findIntersectionValues([2, 3, 2], [1, 2])
print(result)  # Output: [2, 1]
