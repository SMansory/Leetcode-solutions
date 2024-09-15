"""
Problem: Richest customer wealth
Summary: Given an m x n integer grid 'accounts' where 'accounts[i][j]' is the amount of money the ith customer has in the jth bank, return the wealth of the richest customer.
A customer's wealth is the sum of money in all their bank accounts.
Method: Use a generator expression to calculate the sum of each customer's wealth and return the maximum value.
Time complexity: O(m * n), where m is the number of customers and n is the number of banks.
Space complexity: O(1)
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Calculate the wealth of each customer and return the maximum wealth
        return (max(sum(customar_wealth) for customar_wealth in accounts))


# Example usage
result = Solution().maximumWealth([[1, 2, 3], [3, 2, 1]])
print(result)  # Output: 6
