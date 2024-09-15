"""
Problem: Concatenate two arrays
Summary: Given an integer array 'nums' of length 'n',
create an array 'ans' of length '2n' where 'ans[i] == nums[i]' and 'ans[i + n] == nums[i]' for '0 <= i < n'.
Specifically, 'ans' is the concatenation of two 'nums' arrays.
Method: Array concatenation - Use the multiplication operator to concatenate the array with itself.
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution(object):
    def getConcatenation(self, nums):
        # Concatenate the array with itself
        ans = nums * 2
      
        return ans


# Example usage
result = Solution().getConcatenation([1, 2, 1])
print(result)  # Output: [1, 2, 1, 1, 2, 1]
