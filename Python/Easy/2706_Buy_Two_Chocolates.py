"""

Question: Buy two chocolates

Summary: Given an integer array 'prices' representing the prices of chocolates in a store 
and an integer 'money' representing your initial amount of money,
buy exactly two chocolates such that you still have some non-negative leftover money. 
Minimize the sum of the prices of the two chocolates you buy.
Return the amount of money left after buying the two chocolates. 
If it’s not possible to buy two chocolates without going into debt, return the initial amount of money.

Method: Sort the prices and check if the sum of the two cheapest chocolates is within the budget.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        # Calculate the sum of the two cheapest chocolates
        for i in range(len(prices)):
            x = prices[0] + prices[1]
            # Check if the total cost is within the budget
            if money >= x:
                y = x - money
                return abs(y)
              
        return money


# Example usage
result = Solution().buyChoco([1, 2, 2], 3)
print(result)  # Output: 0
