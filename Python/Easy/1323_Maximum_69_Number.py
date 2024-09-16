"""

Question: Maximum 69 number

Summary: Given a positive integer 'num' consisting only of the digits 6 and 9, 
return the maximum number you can obtain by changing at most one digit (6 becomes 9, and 9 becomes 6).

Method: Convert the number to a string, replace the first occurrence of the digit 6 with 9, and convert it back to an integer.

Time complexity: O(n), where n is the number of digits in the number.
Space complexity: O(n)
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the number to a string and replace the first occurence of 6 with 9
        return int(str(num).replace("6", "9", 1))


# Example usage
result = Solution().maximum69Number(9669)
print(result)  # Output: 9969
