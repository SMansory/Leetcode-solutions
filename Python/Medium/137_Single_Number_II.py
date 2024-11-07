"""

Question: Single number II

Summary: Given an integer array 'nums' where every element appears three times except for one, which appears exactly once, 
find the single element. The solution must have linear runtime complexity and use only constant extra space.

Method: Use a counter to keep track of the frequency of each element in the array. 
Iterate through the counter to find and return the element that appears exactly once.

Time complexity: O(n)
Space complexity: O(1)
"""

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
      
        for key, value in counter.items():
            if value==1:
                return key


# Example usage
result = Solution().singleNumber([2, 2, 3, 2])
print(result)  # Output: 3
