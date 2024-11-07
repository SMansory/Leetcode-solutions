"""

Question: Closest divisors

Summary: Given an integer 'num', find the closest two integers in absolute difference whose product equals 
'num + 1' or 'num + 2'. Return both of the integers in any order.

Method: Increment the given number by 1 and 2 to obtain 'num1' and 'num2'. 
Iterate from the square root of 'num + 2' down to 1 to find the divisors of 'num1' or 'num2'. 
Return the pair of divisors when found.

Time complexity: O(√n) - Iterating from the square root of 'num + 2' down to 1 to find the divisors.
Space complexity: O(1)
"""

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num1 = num + 1
        num2 = num + 2
      
        for i in range(isqrt(num + 2), 0, -1):
            if num1 % i == 0:
                return i, num1 // i
            if num2 % i == 0:
                return i, num2 // i


# Example usage 
result = Solution().closestDivisors(8)
print(result)  # Output: [3, 3]
