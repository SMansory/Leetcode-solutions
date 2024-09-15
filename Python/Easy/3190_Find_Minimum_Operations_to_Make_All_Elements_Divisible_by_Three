"""
Problem: Minimum operations to make all elements divisible by 3
Summary: Given an integer array 'nums', determine the minimum number of operations needed to make all elements divisible by 3. 
An operation consists of adding or subtracting 1 from any element.
Method: Iterate through the array and count elements that are not divisible by 3.
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                count += 1

        return count


# Example usage
result = Solution().minimumOperations([1, 2, 3, 4])
print(result)  # Output: 3
