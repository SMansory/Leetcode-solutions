"""

Question: Number of common factors 

Summary: Given two positive integers 'a' and 'b', determine the number of common factors they share. 
An integer 'x' is a common factor of 'a' and 'b' if 'x' divides both 'a' and 'b' without leaving a remainder.

Method: Iterate through all integers from 1 to the minimum of 'a' and 'b',
and count how many of these integers are factors of both 'a' and 'b'.

Time complexity: O(min(a, b))
Space complexity: O(1)
"""

class Solution:
    def commonFactors(self, num1: int, num2: int) -> int:
        ans = 0
      
        for num in range(1, min(num1, num2) + 1):
            if num1 % num == 0 and num2 % num == 0:
                ans += 1
              
        return ans


# Example usage
result = Solution().commonFactors(12, 6)
print(result)  # Output: 4
