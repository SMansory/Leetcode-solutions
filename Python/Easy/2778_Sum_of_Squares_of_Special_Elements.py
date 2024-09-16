"""

Question: Sum of squares of special elements

Summary: Given a 1-indexed integer array 'nums' of length 'n',
an element 'nums[i]' is called special if 'i' divides 'n' (i.e., n % i == 0). 
Return the sum of the squares of all special elements in 'nums'.

Method: Iterate through the array, identify the special elements, and compute the sum of their squares.

Time complexity: O(n), where n is the length of the array.
Space complexity: O(1)
"""

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the sum of squares of special elements 
        return sum(nums[i] ** 2 for i in range(0, len(nums)) if n % (i + 1) == 0)


# Example usage
result = Solution().sumOfSquares([1, 2, 3, 4])
print(result)  # Output: 21
