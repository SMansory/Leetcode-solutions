"""

Question: Percentage of letter in string

Summary: Given a string 's' and a character 'letter', return the percentage of characters in 's' that are equal to 'letter', 
rounded down to the nearest whole percent.

Method: Count the occurrences of 'letter' in the string 's', 
then calculate the percentage of these occurrences relative to the length of the string.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
      
        # Count the occurrences of the letter in the string
        if letter in s:
            count += s.count(letter)

        # Calculate the percentage and round down to the nearest whole percent
        return int((count / len(s)) * 100)


# Example usage
result = Solution().percentageLetter("foobar", "o")
print(result)  # Output: 33
