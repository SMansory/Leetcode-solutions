"""

Question: A number after a double reversal

Summary: Given an integer 'num', reverse its digits to get 'reversed1', then reverse 'reversed1' to get 'reversed2'.
Return true if 'reversed2' equals 'num', otherwise return false.

Method: Convert the integer to a string and check if it has more than one digit and ends with ‘0’. 
If so, return false; otherwise, return true.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return False if len(str(num)) > 1 and str(num)[-1] == "0" else True


# Example usage
result = Solution().isSameAfterReversals(526)
print(result)  # Output: true
