"""
Problem: Build array from aermutation
Summary: Given a zero-based permutation 'nums', create an array 'ans' where 'ans[i] = nums[nums[i]]' for each '0 <= i < nums.length'. 
Return the array 'ans'.
Method: Direct indexing - Iterate through the array and build the result using direct indexing.
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arr = []
      
        for i in range(0, len(nums)):
            arr.append(nums[nums[i]])
          
        return arr


# Example usage
result = Solution().buildArray([0, 2, 1, 5, 3, 4])
print(result)  # Output: [0, 1, 2, 4, 5, 3]
        
