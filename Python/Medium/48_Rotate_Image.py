"""

Question: Rotate image

Summary: Given an n x n 2D 'matrix' representing an image, rotate the image by 90 degrees clockwise in-place. 
This means modifying the input 2D matrix directly without allocating another 2D matrix.

Method: First, transpose the matrix by swapping elements symmetrically across the diagonal. 
Then, reverse each row to achieve the 90 degrees clockwise rotation.

Time complexity: O(n^2) - where 'n' is the number of rows (or columns) in the matrix.
Space complexity: O(1) - The rotation is done in-place without using extra space.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
              
        for row in matrix:
            row.reverse()


# Example usage
result = Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
