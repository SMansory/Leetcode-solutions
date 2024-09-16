"""

Question: Create target array in the given order

Summary: Given two arrays of integers 'nums' and 'index', 
create a target array by inserting the values from 'nums' at the positions specified by 'index'.
Initially, the target array is empty. Read 'nums[i]' and 'index[i]' from left to right, 
and insert 'nums[i]' at 'index[i]' in the target array. Return the target array.

Method: Iterate through the 'index' array and insert the corresponding value from 'nums' at the specified position in the target array.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        # Iterate through the 'index' array and insert values into the 'target' array
        for i in range(len(index)):
                target.insert(index[i], nums[i])
          
        return target


# Example usage
result = Solution().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])
print(result)  # Output: [0, 4, 1, 3, 2]
