"""
Problem: Maximum achievable number
Summary: Given two integers, 'num' and 't', find the maximum achievable number after applying the operation 
(increase or decrease both the number and 'num' by 1) at most 't' times.
Method: Mathematical calculation - The maximum achievable number is 'num + 2 * t'.
Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
       return num + 2 * t  
        

# Example usage
result = Solution().theMaximumAchievableX(4, 1)
print(result)  # Output: 6
