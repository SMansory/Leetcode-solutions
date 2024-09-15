"""
Problem: Final value of variable after performing operations
Summary: Given an array of strings 'operations', 
return the final value of the variable 'X' after performing all the operations. 
The operations are:
- '++X' and 'X++' increment the value of 'X' by 1.
- '--X' and 'X--' decrement the value of 'X' by 1.
Initially, the value of 'X' is 0.
Method: Iterate through the operations and update the value of 'X' accordingly.
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
      
        for i in operations:
            if i == "X++" or i == "++X":
                x += 1
            elif i == "X--" or i == "--X":
                x -= 1
              
        return x


# Example usage
result = Solution().finalValueAfterOperations(["--X", "X++", "X++"])
print(result)  # Output: 1
