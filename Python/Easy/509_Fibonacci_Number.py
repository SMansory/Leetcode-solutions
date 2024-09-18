"""

Question: Fibonacci number

Summary: The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
Given an integer 'n', compute the nth Fibonacci number.

Method: Use an iterative approach to calculate the Fibonacci number by updating two variables in a loop.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
      
        for _ in range(n):
            # Update 'a' and 'b' to the next fibonacci numbers
            a, b = b, a + b
          
        return a


# Example usage
result = Solution().fib(2)
print(result)  # Output: 1
