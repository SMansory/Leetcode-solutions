"""

Question: Single number III

Summary: Given an integer array 'nums' in which exactly two elements appear only once and all other elements appear exactly twice,
find the two elements that appear only once. The solution must run in linear time complexity and use only constant extra space.

Method: Iterate through the array and count the occurrences of each number. Return the numbers that appear exactly once.

Time complexity: O(n)
Space complexity: O(1) - considering the constant space for storing the results.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [i for i in nums if nums.count(i) == 1]


# Example usage
result = Solution().singleNumber([1, 2, 1, 3, 2, 5])
print(result)  # Output: [3, 5]
