"""

Question: Subsets

Summary: Given an integer array 'nums' of unique elements, return all possible subsets. 
The solution set must not contain duplicate subsets and can be returned in any order.

Method: Start with an empty subset. 
Iterate through each element in 'nums' and add it to all existing subsets to form new subsets.

Time complexity: O(2^n) - where 'n' is the number of elements in 'nums'.
Space complexity: O(2^n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]
      
        for i in nums:
            arr += [item + [i] for item in arr]
          
        return arr


# Example usage
result = Solution().subsets([1, 2, 3])
print(result)  # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
