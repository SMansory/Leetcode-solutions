"""
Question: Count pairs with sum less than target

Summary: Given a integer array 'nums' of length 'n' and an integer 'target', 
return the number of pairs (i, j) where 0 <= i < j < n and 'nums[i] + nums[j] < target'.

Method: Use nested loops to find and count pairs that satisfy the condition.

Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0

        # Iterate through each pair of indices
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Check if the pair (i, j) satisfies the condition
                if 0 <= i < j < n and nums[i] + nums[j] < target:
                    count += 1
                  
        return count


# Example usage
result = Solution().countPairs([-1, 1, 2, 3, 1], 2)
print(result)  # Output: 3
