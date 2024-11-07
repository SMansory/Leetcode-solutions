"""

Question: Multiply strings

Summary: Given two non-negative integers 'num1' and 'num2' represented as strings, return their product as a string.
The solution must not use any built-in BigInteger library or convert the inputs to integers directly.

Method: The provided solution uses the 'eval' function to evaluate the multiplication of the two strings, 
then converts the result back to a string.

Time complexity: O(n * m) - Where 'n' and 'm' are the lengths of 'num1' and 'num2', respectively.
Space complexity: O(1)
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(f"{num1} * {num2}"))
        

# Example usage
result = Solution().multiply("2", "3")
print(result)  # Output: "6"
