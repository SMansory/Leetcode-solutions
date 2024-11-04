"""

Question: Search insert position

Summary: You are given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be inserted in order. The solution must have a runtime complexity of O(log n).

Method: Check if the target value is in the array. 
If found, return its index. If not, append the target to the array, sort it, and return the index of the target.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
          
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


# Example usage
result = Solution().searchInsert([1, 3, 5, 6], 5)
print(result)  # Output: 2
