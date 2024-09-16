"""

Question: Minimum operations to exceed threshold value I

Summary: Given a 0-indexed integer array 'nums' and an integer 'k',
return the minimum number of operations needed so that all elements in the array are greater than or equal to 'k'.
In one operation, you can remove one occurrence of the smallest element in 'nums'.

Method: Iterate through the array and count the elements that are greater than or equal to 'k'.
The minimum number of operations is the difference between the total number of elements and
the count of elements that are greater than or equal to 'k'.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = []
      
        # Iterate through the array and collect elements >= 'k'
        for i in nums:
            if i >= k:
                arr.append(i)
              
        # Return the number of operations needed
        return len(nums) - len(arr)


# Example usage
result = Solution().minOperations([2, 11, 10, 1, 3], 10)
print(result)  # Output: 3
