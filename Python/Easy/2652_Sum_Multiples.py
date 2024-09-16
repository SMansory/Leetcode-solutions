"""

Question: Sum multiples

Summary: Given a positive integer 'n', find the sum of all integers in the range '[1, n]' that are divisible by 3, 5, or 7.
Return the sum of these numbers.

Method: Iterate through the range '[1, n]' and check if each number is divisible by 3, 5, or 7. If it is, add it to the 'total sum'.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total_sum = 0
        # Iterate through the range '[1, n]'
        for i in range(1, n + 1):
            # Check if the number 'i' is divisible by 3, 5, or 7
            if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
                total_sum = total_sum + i
              
        return total_sum


# Example usage
result = Solution().sumOfMultiples(7)
print(result)  # Output: 21
