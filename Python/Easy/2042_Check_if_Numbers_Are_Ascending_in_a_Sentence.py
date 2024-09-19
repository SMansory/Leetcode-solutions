"""

Question: Check if numbers are ascending in a sentence

Summary: Given a string 's' representing a sentence where tokens are separated by a single space, 
check if all the numbers in the sentence are strictly increasing from left to right. 
Each token is either a positive number (digits 0-9 with no leading zeros) or a word (lowercase English letters).
Return true if the numbers are strictly increasing, otherwise return false.

Method: Split the sentence into tokens, extract the numbers, and check if they are in strictly increasing order.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = []
      
        for i in s.split():
            if i.isnumeric():
                arr.append(int(i))

        # Check if the numbers are in strictly increasing order
        return arr == sorted(set(arr))


# Example usage
result = Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")
print(result)  # Output: true
