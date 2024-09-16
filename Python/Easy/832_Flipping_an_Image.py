"""

Question: Flipping an image 

Summary: Given an ( n \times n ) binary matrix 'image', flip the image horizontally and then invert it. 
Flipping an image horizontally means reversing each row, and inverting an image means replacing each 0 with 1 and each 1 with 0.

Method: Iterate through each row of the matrix, reverse the row, and then invert each element in the row.

Time complexity: O(n^2), where n is the number of rows (or columns) in the matrix.
Space complexity: O(n^2)
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []

        # Iterate through each row of the matrix
        for i in image:
            # Reverse the row
            i.reverse()
            # Invert each element in the row
            res.append([x ^ 1 for x in i])
          
        return res


# Example usage
result = Solution().flipAndInvertImage([[1, 1, 0],[1, 0, 1],[0, 0, 0]])
print(result)  # Output: [[1, 0, 0],[0, 1, 0],[1, 1, 1]]
