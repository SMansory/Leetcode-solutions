"""

Question: Maximum number of consecutive values you can make

Summary: Given an integer array 'coins' where each element represents the value of a coin,
return the maximum number of consecutive integer values that can be made with the coins starting from and including 0.

Method: Sort the coins in ascending order and iterate through them. For each coin, 
check if it can be used to extend the current range of consecutive sums. 
If a coin value exceeds the current maximum sum that can be formed plus one, stop the iteration.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        c = 1
      
        for i in coins:
            if i > c:
                break
            else:
                c += i
              
        return c


# Example usage
result = Solution().getMaximumConsecutive([1, 3])
print(result)  # Output: 2
