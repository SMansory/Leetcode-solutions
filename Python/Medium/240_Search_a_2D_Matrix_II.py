"""

Question: Search a 2D matrix II

Summary: Write an algorithm to search for a value target in an 'm x n' integer matrix with the following properties: 
integers in each row are sorted in ascending order from left to right,
and integers in each column are sorted in ascending order from top to bottom.

Method: Use a generator expression within the 'any' function to check if the target value exists in any row of the matrix.

Time complexity: O(m * n) - 'm' represents the number of rows in the matrix, and 'n' represents the number of columns.
Space complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in i for i in matrix)


# Example usage
result = Solution().searchMatrix([[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]], 5)
print(result)  # Output: true
