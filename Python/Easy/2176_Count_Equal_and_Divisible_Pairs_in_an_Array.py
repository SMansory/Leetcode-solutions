"""

Question: Count equal and divisible pairs in an array

Summary: Given a 0-indexed integer array 'nums' of length 'n' and an integer 'k', 
find the number of pairs ((i, j)) where (0 <= i < j < n), 
such that 'nums[i]' equals 'nums[j]' and (i * j) is divisible by 'k'.

Method: Use nested loops to iterate through all possible pairs of indices and count those that satisfy the given conditions.

Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
      
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] == nums[j]) and ((i * j) % k == 0):
                    count += 1
                  
        return count


# Example usage
result = Solution().countPairs([3, 1, 2, 2, 2, 1, 3], 2)
print(result)  # Output: 4
