"""

Question: Ugly number

Summary: An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
You are given an integer 'n', return true if 'n' is an ugly number.

Method: 
1. Check if 'n' is less than or equal to 0; if so, return False.
2. Continuously divide 'n' by 2, 3, and 5 while it is divisible by these numbers.
3. After the loop, if 'n' equals 1, return True; otherwise, return False.

Time complexity: O(log n)
Space complexity: O(1)
"""

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
          
        while n % 2 == 0:
            n //= 2
          
        while n % 3 == 0:
            n //= 3
          
        while n % 5 == 0:
            n //= 5
          
        return n == 1


# Example usage
result = Solution().isUgly(6)
print(result)  # Output: true
