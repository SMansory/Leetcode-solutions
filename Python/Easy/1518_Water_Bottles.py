"""

Question: Water bottles

Summary: Given 'numBottles' full water bottles and the ability to exchange numExchange empty bottles for one full bottle,
determine the maximum number of water bottles you can drink. Drinking a full bottle turns it into an empty bottle.

Method: Use a mathematical approach to calculate the total number of bottles you can drink 
by considering the initial bottles and the exchanges.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Calculate the total number of bottles you can drink
        return numBottles + (numBottles - 1) // (numExchange - 1)


# Example usage
result = Solution().numWaterBottles(9, 3)
print(result)  # Output: 13
