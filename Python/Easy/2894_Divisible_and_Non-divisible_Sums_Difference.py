"""
Problem: Difference of sums
Summary: Given two positive integers 'n' and 'm', 
calculate the difference between the sum of all integers in the range '[1, n]' 
that are not divisible by 'm' and the sum of all integers in the same range that are divisible by 'm'. 
Return the result as 'num1 - num2'.
Method: Iterate through the range and sum the integers based on their divisibility by 'm'.
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
      
        for i in range(1, n + 1):
            if i % m == 0:
                num1 += i
            else:
                num2 += i
              
        return num2 - num1


# Example usage
result = Solution().differenceOfSums(10, 3)  
print(result)  # Output: 19
