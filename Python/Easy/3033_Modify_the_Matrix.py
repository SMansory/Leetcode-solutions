"""

Question: Modify the matrix

Summary: Given a 0-indexed 'm x n' integer 'matrix', 
create a new matrix 'answer' that is initially a copy of the original matrix.
Replace each element with the value -1 with the maximum element in its respective column. Return the modified matrix.

Method: Iterate through each column to find the maximum value,
then replace all -1 values in that column with the maximum value.

Time complexity: O(m * n)
Space complexity: O(1)
"""

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Number of columns in the matrix
        m = len(matrix[0])
      
        for i in range(m):
            # Initialize the maximum value for the current column
            max_val = 0
            for j in range(len(matrix)):
                # Find the maximum value in the current column
                max_val = max(max_val, matrix[j][i])
            for j in range(len(matrix)):
                # Replace -1 with the maximum value in the column
                if matrix[j][i] == -1:
                    matrix[j][i] = max_val
                  
        return matrix


# Example usage
result = Solution().modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]])
print(result)  # Output: [[1, 2, 9], [4, 8, 6], [7, 8, 9]]
