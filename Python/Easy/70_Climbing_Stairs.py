"""

Question: Climbing stairs

Summary: Given that it takes 'n' steps to reach the top of a staircase, and you can climb either 1 or 2 steps at a time,
return the number of distinct ways to reach the top.

Method: Use dynamic programming to iteratively calculate the number of ways to reach each step,
maintaining only the last two results for space efficiency.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        x, y = 0, 1
      
        for i in range(n):
            x, y = y, x + y
        return y 


# Example usage
result = Solution().climbStairs(2)
print(result)  # Output: 2
