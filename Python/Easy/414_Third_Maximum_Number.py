"""

Question: Third maximum number

Summary: Given an integer array 'nums', return the third distinct maximum number in the array. 
If the third maximum does not exist, return the maximum number.

Method: Convert the array to a set to remove duplicates, then sort the set in descending order.
If the length of the set is at least 3, return the third element; otherwise, return the maximum element.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Remove duplicates by converting to a set
        nums = list(set(nums))
        # Sort the set in descending order
        nums.sort()
        nums = nums[::-1]

        # If there are at least 3 distinct numbers, return the third largest
        if len(nums) >= 3:
            return nums[2]

        # Otherwise, return the largest number
        return max(nums)


# Example usage
result = Solution().thirdMax([3, 2, 1])
print(result)  # Output: 1
