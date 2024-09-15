"""
Problem: Score of a String
Summary: Given a string s, calculate the score of the string. 
The score is defined as the sum of the absolute differences between the ASCII values of each pair of adjacent characters in the string.
Method: Sliding Window - Iterate through the string, calculate the absolute differences between ASCII values of adjacent characters, and sum these differences
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Convert each character in the string to its ASCII value
        ascii_values = [ord(char) for char in s]
      
        # Initialize the score to 0
        score = 0

        # Iterate through the ASCII valus and calculate the absolute differences
        for num in range(0, len(ascii_values) - 1):
            difference = abs(ascii_values[num] - ascii_values[num + 1])
            score = score + difference
          
        return score           


# Example usage
ret = Solution().scoreOfString("zaz")
print(ret)  # Output: 50
