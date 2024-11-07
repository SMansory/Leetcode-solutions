"""

Question: Super pow

Summary: Given a positive integer 'a' and a very large positive integer 'b' represented as an array, 
compute a to the power of b mod 1337.

Method: Convert the array 'b' to an integer and use the 'pow' function to calculate the power with modulus.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = ""
      
        for digit in b:
            num += str(digit)
          
        num = int(num)
      
        return pow(a, num, 1337)


# Example usage
result = Solution().superPow(2, [3])
print(result)  # Output: 8
