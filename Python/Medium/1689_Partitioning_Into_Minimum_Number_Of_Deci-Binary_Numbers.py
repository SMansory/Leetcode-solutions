"""

Question: Partitioning into minimum number of deci-binary numbers

Summary: Given a string 'n' that represents a positive decimal integer,
return the minimum number of positive deci-binary numbers needed so that they sum up to 'n'. 
A deci-binary number is a decimal number where each digit is either 0 or 1 without any leading zeros.

Method: Find the maximum digit in the string 'n' and return it as an integer. 
This represents the minimum number of deci-binary numbers needed.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        # Find the maximum digit in the string and return it as an integer
        return int(max(n))


# Example usage
result = Solution().minPartitions("32")
print(result)  # Output: 3
