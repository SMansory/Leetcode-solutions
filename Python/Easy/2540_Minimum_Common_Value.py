"""

Question: Minimum common value


Summary: Given two integer arrays 'nums1' and 'nums2', both sorted in non-decreasing order,
return the smallest integer that is common to both arrays. If there is no common integer, return -1.


Method: Convert both arrays to sets and find their intersection. 
If the intersection is non-empty, return the smallest element; otherwise, return -1.


Time complexity: O(n + m) where 'n' and 'm' are the lengths of 'nums1' and 'nums2' respectively.
Space complexity: O(n + m) for storing the sets.
"""

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Convert both arrays to sets
        nums1 = set(nums1)
        nums2 = set(nums2)

        # Find the intersection of both sets
        result = nums1.intersection(nums2)

        # Return the smallest element in the intersection if it exists
        if result:
            return min(result)
        return -1


# Example usage
result = Solution().getCommon([1, 2, 3], [2, 4])
print(result)  # Output: 2
