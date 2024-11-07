"""

Question: Search a 2D matrix

Summary: Given an 'm x n' integer matrix with each row sorted in non-decreasing order and 
each first integer of a row greater than the last integer of the previous row, 
find out if a 'target' integer is present in the matrix. The solution should have a time complexity of O(log(m * n)).

Method: Flatten the matrix into a single list and check if the target value is present in it.

Time complexity: O(m * n) - Where 'm' is the number of rows and 'n' is the number of columns.
Space complexity: O(m * n)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return True if target in [j for i in matrix for j in i] else False


# Example usage
result = Solution().searchMatrix([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 3)
print(result)  # Output: true
