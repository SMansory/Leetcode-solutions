"""

Question: Determine whether matrix can be obtained by rotation

Summary: Given two 'n x n' binary matrices 'mat' and 'target', 
determine if you can make 'mat' equal to 'target' by rotating 'mat' in 90-degree increments.

Method:
1. Check if 'mat' is already equal to 'target'.
2. Rotate 'mat' by 90 degrees clockwise up to three times.
3. If after any rotation 'mat' becomes equal to 'target', return true.
4. If none of the rotations result in equality, return false.

Time Complexity: O(n^2) (where 'n' is the number of rows/columns in the matrix)
Space Complexity: O(1) (constant space, in-place modifications)
"""

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        for k in range(3):
            for i in range(len(mat)):
                for j in range(i, len(mat[0])):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in range(len(mat)):
                mat[row].reverse()

            if mat == target:
                return True
                
        return False



# Example usage
result = Solution().findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]])
print(result)  # Output: true
