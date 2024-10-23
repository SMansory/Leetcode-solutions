"""

Question: Happy number

Summary: Write an algorithm to check if a number 'n' is a happy number.
A happy number is defined by the process where you replace the number by the sum of the squares of its digits and 
repeat until the number equals 1, or it loops endlessly in a cycle that does not include 1. 
Return true if 'n' is a happy number, and false if it's not.

Method: Recursively calculate the sum of the squares of the digits of 'n'. If n becomes 1, it is a happy number.
If 'n' becomes 4, it will loop endlessly (as 4 is known to be part of the loop for unhappy numbers).

Time Complexity: O(log n) (due to repeatedly processing the digits of 'n')
Space Complexity: O(log n) (due to recursion stack)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        a = 0 
        
        if n == 1:
            return True
        if n == 4:
            return False
        for i in str(n):
            a += int(i) * int(i)

        n = a
        return Solution.isHappy(self, n)


# Example usage
result = Solution().isHappy(19)
print(result)  # Output: true
