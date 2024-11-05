"""

Question: Sort the students by their kth score

Summary: Sort the students (rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.

Method: Use the sorted() function with a custom key to sort the rows based on the scores in the kth exam.
Reverse the order to get the highest scores first.

Time complexity: O(m log m)
Space complexity: O(m)
"""

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]: 
        # Sort the rows of the matrix by the k-th exam scores in descending order
        return sorted(score, key=lambda x: x[k])[::-1]


# Example usage
result = Solution().sortTheStudents([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2)
print(result)  # Output: [[7, 5, 11, 2], [10, 6, 9, 1], [4, 8, 3, 15]]
