"""

Question: Two sum

Summary: You are given an array of integers 'nums' and an integer 'target', 
return indices of the two numbers such that they add up to 'target'. 
Each input will have exactly one solution, and you may not use the same element twice.
The answer can be returned in any order.

Method: Use two nested loops to iterate through the array and find the pair of indices whose elements sum up to the 'target'.

Time complexity: O(n^2) (due to the nested loops)
Space complexity: O(1)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]
        return []


# Example usage
result = Solution().twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]
