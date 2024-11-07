"""

Question: Reverse integer

Summary: Given a 32-bit signed integer 'x', return 'x' with its digits reversed.
If reversing 'x' causes the value to go outside the 32-bit integer range [−2 to the power of 31,2 to the power of 31 − 1],
return 0. Assume the environment does not support storing 64-bit integers.

Method: Check if the integer is negative. 
If it is, reverse the digits excluding the negative sign and add the negative sign back. 
If the reversed number is outside the 32-bit range, return 0. If the integer is positive, simply reverse the digits. 
Again, return 0 if the reversed number is outside the 32-bit range.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == "-":
            y = str(x)[1:]
            z = "-" + y[::-1]
            z = int(z)
            if z > 2 ** 31:
                return 0
            if z < -2 ** 31:
                return 0
            else:
                return z
              
        else:
            y = str(x)[::-1]
            y = int(y)
            if y > 2 ** 31:
                return 0
            if y < -2 ** 31:
                return 0
            else:
                return y


# Example usage
result = Solution().reverse(123)
print(result)  # Output: 321
