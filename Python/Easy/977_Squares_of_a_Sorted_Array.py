"""

Question: Squares of a sorted array

Summary: Given an integer array 'nums' sorted in non-decreasing order, 
return an array containing the squares of each number, also sorted in non-decreasing order.

Method: Square each element in the array and then sort the resulting array.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Square each element and store in result
        result = [abs(i)**2 for i in nums]
        # Sort the squared elements
        result.sort()
      
        return result


# Example usage
result = Solution().sortedSquares([-4, -1, 0, 3, 10])
print(result)  # Output: [0, 1, 9, 16, 100]
