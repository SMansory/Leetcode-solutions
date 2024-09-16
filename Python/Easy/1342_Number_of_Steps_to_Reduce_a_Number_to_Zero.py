"""

Question: Number of steps to reduce a number to zero

Summary: Given an integer 'num', determine the number of steps required to reduce it to zero.
If the current number is even, divide it by 2; if it is odd, subtract 1 from it.

Method: Use a loop to repeatedly divide the number by 2 if it is even, 
or subtract 1 if it is odd, until the number becomes zero. Count the number of steps taken.

Time complexity: O(log n).
Space complexity: O(1)
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        # Loop until the 'num' is reduced to 0
        while num > 0:
            # If the number is even, divide it by 2
            if num % 2 == 0:
                 num = num // 2  
            # If the number is odd, subtract 1 from it
            else:
                num = num - 1
            steps += 1   
          
        return steps


# Example usage
result = Solution().numberOfSteps(14)
print(result)  # Output: 6
