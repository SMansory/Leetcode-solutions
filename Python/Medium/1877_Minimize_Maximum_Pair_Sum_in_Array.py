"""

Question: Minimize maximum pair sum in array

Summary: Given an array 'nums' of even length 'n', 
pair up the elements into n / 2 pairs such that each element is in exactly one pair and the maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements. 
The pair sum of a pair (a, b) is equal to a + b, and the maximum pair sum is the largest pair sum in a list of pairs.

Method: Sort the array and pair the smallest element with the largest element, the second smallest with the second largest,
and so on. Calculate the maximum pair sum for these pairs and return the minimized maximum pair sum.

Time complexity: O(n log n) - Sorting the array takes O(n log n) time.
Space complexity: O(1)
"""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
      
        for num in range(len(nums) // 2):
            result = max(result, nums[num] + nums[len(nums) - 1 - num])
          
        return result


# Example usage
result = Solution().minPairSum([3, 5, 2, 3])
print(result)  # Output: 7
