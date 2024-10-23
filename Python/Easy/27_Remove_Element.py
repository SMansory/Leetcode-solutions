"""

Question: Remove element


Summary: Given an array of integers and a specified value, remove all instances of that value in-place.
The order of elements can change. Return the count of elements in the array that do not match the specified value.


Method: Iterate through the array, using the remove method to delete the specified value whenever it is encountered.


Time Complexity: O(n^2) (due to the repeated calls to remove method inside a loop)
Space Complexity: O(1) (constant space, as the removal is done in-place)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
          
        return len(nums)


# Example usage
result = Solution().removeElement([3, 2, 2, 3], 3)
print(result)  # Output: [2, 2]
