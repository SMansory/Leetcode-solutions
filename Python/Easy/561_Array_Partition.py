"""

Question: Array partition

Summary: Given an integer array 'nums' of '2n' elements,
group these integers into 'n' pairs ((a1, b1), (a2, b2), …, (an, bn)) such that the sum of the minimum values of each pair is maximized.
Return this maximized sum.

Method: Sort the array and sum up every second element starting from the first element.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
      
        for i in range(len(nums)):
            if i % 2 == 0:
                ans += nums[i]
              
        return ans


# Example usage
result = Solution().arrayPairSum([1, 4, 3, 2])
print(result)  # Output: 4
