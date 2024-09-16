"""

Question: Height checker 

Summary: Given an integer array 'heights' representing the current order of students standing in a line,
and an integer array 'expected' representing the expected order of students by height, 
return the number of indices where 'heights[i]' does not match 'expected[i]'.

Method: Sort the 'heights' array to get the expected order, 
then compare each element of 'heights' with the corresponding element in the 'expected' array to count the mismatches.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
      
        for counts in range(len(heights)):
            if heights[counts] != expected[counts]:
                count += 1
              
        return count


# Example usage
result = Solution().heightChecker([1, 1, 4, 2, 1, 3])
print(result)  # Output: 3
