"""

Question: Find the duplicate number

Summary: Given an array 'nums' of length 'n + 1' containing integers in the range [1, n], find the single repeated number. 
The solution must not modify the array and must use only constant extra space.

Method: Use a counter to track the frequency of each element in the array.
Iterate through the counter to find and return the element that appears more than once.

Time complexity: O(n)
Space complexity: O(n)
"""

from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = Counter(nums)
      
        for key, value in num.items():
            if value > 1:
                return key


# Example usage
result = Solution().findDuplicate([1, 3, 4, 2, 2])
print(result)  # Output: 2
