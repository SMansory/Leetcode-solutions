"""

Question: Valid sudoku

Summary: Determine if a 9 x 9 Sudoku board is valid by checking that each row, column,
and 3 x 3 sub-box contains the digits 1-9 without repetition. Only the filled cells need to be validated.

Method: Iterate through the board and collect tuples representing the row, column, 
and sub-box constraints for each filled cell. Use a set to ensure all collected tuples are unique.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = []
      
        for i in range(9):
            for j in range(9):
                a = board[i][j]
                if a != '.':
                    result += [(i, a), (a, j), (i // 3, j // 3, a)]
                  
        return len(result) == len(set(result))


# Example usage
result = Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."],
                                   ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"],
                                   [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]])
print(result)  # Output: true
