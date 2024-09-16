"""

Question: Harshad number

Summary: An integer is called a Harshad number if it is divisible by the sum of its digits.
Given an integer 'x', return the sum of its digits if 'x' is a Harshad number; otherwise, return -1.

Method: Calculate the sum of the digits of 'x', check if 'x' is divisible by this sum, and return the sum if true, otherwise return -1.

Time complexity: O(d), where d is the number of digits in 'x'.
Space complexity: O(1)
"""

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # Calculate sum of the digits
        digits = sum([int(digit) for digit in str(x)])

        # Check if 'x' is divisible by the sum of its digits
        if x % digits == 0:
            return digits
        return -1


# Example usage
result = Solution().sumOfTheDigitsOfHarshadNumber(18)
print(result)  # Output: 9
