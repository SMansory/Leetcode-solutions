"""

Question: Count the Digits that Divide a Number

Summary: Given an integer 'num', return the number of digits in 'num' that divide 'num' without leaving a remainder.

Method: Iterate through each digit of the number, check if it divides the number evenly, and count such digits.

Time complexity: O(d), where 'd' is the number of digits in the number.
Space complexity: O(1)
"""


class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        x = num

        # Iterate through each digit of the number
        while x:
            digit = x % 10
            # Check if the digit divides the number evenly
            if num % digit == 0:
                count += 1
            x //= 10
          
        return count


# Example usage
result = Solution().countDigits(7)
print(result)  # Output: 1
