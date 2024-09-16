"""

Question: Split a balanced string into the maximum number of balanced substrings

Summary: Given a balanced string s containing an equal number of 'L' and 'R' characters,
split it into the maximum number of balanced substrings. Each substring must have an equal number of 'L' and 'R' characters.

Method: Iterate through the string, counting 'L' and 'R' characters. 
When the counts are equal, increment the count of balanced substrings and reset the counters.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        count = 0

        # Iterate through the string 
        for char in s:
            if char == "L":
                l += 1
            elif char == "R":
                r += 1
            # When counts are equal, increment count and reset counters
            if l == r:
                count += 1
                l = 0
                r = 0
              
        return count


# Example usage
result = Solution().balancedStringSplit("RLRRLLRLRL")
print(result)  # Output: 4
