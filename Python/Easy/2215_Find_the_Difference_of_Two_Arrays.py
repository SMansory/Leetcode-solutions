"""

Question: Find the difference of two arrays

Summary: Given two 0-indexed integer arrays 'nums1' and 'nums2', return a list answer of size 2 where:
1. 'answer[0]' contains all distinct integers in 'nums1' that are not present in 'nums2'.
2. 'answer[1]' contains all distinct integers in 'nums2' that are not present in 'nums1'. 
The integers in the lists can be returned in any order.

Method: Convert both arrays to sets to find the distinct elements,
then use set operations to determine the differences between the two sets.

Time complexity: O(n + m), where n is the length of 'nums1' and m is the length of 'nums2'.
Space complexity: O(n + m)
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
      
        a = list(nums1_set.difference(nums2_set))
        b = list(nums2_set.difference(nums1_set))
      
        return [a,b]


# Example usage
result = Solution().findDifference([1, 2, 3], [2, 4, 6])
print(result)  # Output: [[1, 3], [4, 6]]

