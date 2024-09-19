"""

Question: Smallest range I

Summary: Given an integer array 'nums' and an integer 'k',
you can change any element 'nums[i]' to 'nums[i] + x' where 'x' is an integer from the range '[-k, k]'.
You can apply this operation at most once for each index.
The score of 'nums' is the difference between the maximum and minimum elements.
Return the minimum score of 'nums' after applying the operation.

Method: Calculate the potential new minimum and maximum values after applying the operation, 
then compute the difference between these values.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # Calculate the potential new minimum and maximum values
        a = min(nums) + k 
        b = max(max(nums) - k, a)

        # Return the difference between the new maximum and minimum values
        return b - a


# Example usage
result = Solution().smallestRangeI([1], 0)
print(result)  # Output: 0
