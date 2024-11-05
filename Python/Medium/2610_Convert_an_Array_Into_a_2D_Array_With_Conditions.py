"""

Question: Convert an array into a 2D array with conditions

Summary: Given an integer array 'nums', 
create a 2D array from 'nums' with distinct integers in each row and minimal number of rows. 
Return the resulting array. If there are multiple answers, return any.

Method: Create a 2D array by iterating through 'nums' and adding distinct integers to each row. 
Remove added integers from 'nums' in each iteration.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr = []
      
        while len(nums):
            # Append a row of distinct integers
            arr.append(list(set(nums)))

            # Remove added integers from 'nums'
            for i in arr[-1]:
                nums.pop(nums.index(i))
              
        return arr


# Example usage
result = Solution().findMatrix([1, 3, 4, 1, 2, 3, 1])
print(result)  # Output: [[1, 3, 4, 2], [1, 3], [1]]
