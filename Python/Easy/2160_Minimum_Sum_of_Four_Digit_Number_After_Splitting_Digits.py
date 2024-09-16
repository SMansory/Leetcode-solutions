"""

Question: Split a four-digit number into two integers to minimize their sum

Summary: Given a positive integer 'num' consisting of exactly four digits,
split 'num' into two new integers 'new1' and 'new2' using all the digits of 'num'. 
Leading zeros are allowed in 'new1' and 'new2'. Return the minimum possible sum of 'new1' and 'new2'.

Method: Sort the digits of num and form the two new integers by pairing the smallest and largest digits to minimize their sum.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def minimumSum(self, num: int) -> int:
        # Sort the digits of the number
        num = sorted(str(num))
        # Form 2 new integers and return their sum
        return int(num[0] + num[2]) + int(num[1] + num[3])


# Example usage
result = Solution().minimumSum(2932)
print(result)  # Output: 52
