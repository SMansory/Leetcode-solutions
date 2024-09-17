"""

Question: Two out of three

Summary: Given three integer arrays 'nums1', 'nums2', and 'nums3',
return a distinct array containing all the values that are present in at least two out of the three arrays. 
The order of the values in the result does not matter.

Method: Use list comprehensions to collect elements that appear in at least two of the three arrays, 
then convert the result to a set to ensure uniqueness.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = set([x for x in nums1 if x in nums2 or x in nums3] + \
               [x for x in nums2 if x in nums1 or x in nums3] + \
               [x for x in nums3 if x in nums1 or x in nums2])
      
        return list(result)


# Example usage
result = Solution().twoOutOfThree([1, 1, 3, 2], [2, 3], [3])
print(result)  # Output: [3, 2]
