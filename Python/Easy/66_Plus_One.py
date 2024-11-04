"""

Question: Plus one

Summary: Given a large integer represented as an array of its digits, ordered from most significant to least significant,
increment the integer by one and return the resulting array of digits.

Method: Convert the array of digits to an integer, increment it by one, and convert the result back to an array of digits.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the array of digits to an integer and increment by one
        ans = int("".join(map(str, digits))) + 1
        # Convert the resulting integer back to an array of digits
        result = [int(digit) for digit in str(ans)]
        return result


# Eample usage
result = Solution().plusOne([1, 2, 3])
print(result)  # Output: [1, 2, 4]
