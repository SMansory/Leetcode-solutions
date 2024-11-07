"""

Question: Integer break

Summary: Given an integer 'n', break it into the sum of 'k' positive integers, where 'k >= 2',
and maximize the product of those integers. Find the maximum product you can get.

Method: If 'n' is less than 4, return 'n - 1' directly as the maximum product. For n greater than or equal to 4, 
iteratively subtract 3 from 'n' and multiply it to the product until 'n' is less than or equal to 4.
Finally, multiply the remaining 'n' with the product to get the maximum product.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
          
        product = 1
        while n > 4:
            product *= 3
            n -= 3
          
        return product * n


# Example usage
result = Solution().integerBreak(2)
print(result)  # Output: 1
