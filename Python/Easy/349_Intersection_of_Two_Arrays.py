"""

Question: Intersection of two arrays

Summary: Given two integer arrays 'nums1' and 'nums2', return an array containing their intersection. 
Each element in the result must be unique, and the order of the elements does not matter.

Method: Convert both arrays to sets to remove duplicates, then find the intersection of these sets.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both arrays to sets to remove duplicates
        nums1 = set(nums1)
        nums2 = set(nums2)
        # Find the intersection of the two sets
        return list(nums1.intersection(nums2))


# Example usage
result = Solution().intersection([1, 2, 2, 1], [2, 2])
print(result)  # Output: [2]
