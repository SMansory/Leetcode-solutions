"""

Question: Add digits

Summary: Given an integer 'num', repeatedly add all its digits until the result has only one digit. 
Return the resulting single digit.

Method: Convert the number to a string to iterate over its digits, sum the digits, 
and repeat the process until the number is a single digit.

Time complexity: O(log n)
Space complexity: O(1)
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            # Convert the number to a string, iterate over its digits, and sum them
            num = sum([int(digit) for digit in str(num)])
          
        return num


# Example usage
result = Solution().addDigits(38)
print(result)  # Output: 2
