"""
Problem: Count good pairs
Summary: Given an array of integers 'nums', determine the number of "good" pairs.
A pair (i, j) is considered good if nums[i] == nums[j] and i < j.
Method: Nested loops - Iterate through the array with two nested loops to count the good pairs.
Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
      
        count = 0
      
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
                  
        return count


# Example usage
result = Solution().numIdenticalPairs([1,2,3,1,1,3])
print(result)  # Output: 4
