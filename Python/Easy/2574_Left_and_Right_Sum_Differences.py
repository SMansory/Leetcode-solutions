"""
Question: Left and right sum differences

Summary: Given a 0-indexed integer array 'nums', 
find a 0-indexed integer array 'answer' where 'answer[i] = |leftSum[i] - rightSum[i]|'.
Here, 'leftSum[i]' is the sum of elements to the left of index 'i' in `nums`, 
and 'rightSum[i]' is the sum of elements to the right of index 'i' in `nums`. 
Return the array 'answer'.

Method: Calculate the left and right sums for each index and find their absolute difference.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Initialize the res list
        res = []

        # Iterate through each index in nums
        for i in range(len(nums)):
            # Append the absolute difference to the res list
            res.append(abs(sum(nums[0:i])-sum(nums[i+1:])))
          
        return res


# Example usage
result = Solution().leftRightDifference([10, 4, 8, 3])
print(result)  # Output: [15, 1, 11, 22]
