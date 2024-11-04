"""

Question: Valid perfect square

Summary: You are given a positive integer 'num', return true if 'num' is a perfect square.
A perfect square is an integer that is the square of another integer. 
Do not use any built-in library functions, such as sqrt.

Method: The approach converts the number to its square root and 
then checks if squaring that root gives back the original number.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num) == floor(sqrt(num))


# Example usage
result = Solution().isPerfectSquare(16)
print(result)  # Output: true
