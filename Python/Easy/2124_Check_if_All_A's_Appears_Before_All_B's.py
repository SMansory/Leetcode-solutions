"""

Question: Check if all a's appears before all b's

Summary: Given a string 's' consisting of only the characters ‘a’ and ‘b’, determine if all 'a’s appear before all 'b’s.
Return true if this condition is met, otherwise return false.

Method: Sort the string and compare it with the original string to check if the order of characters is maintained.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def checkString(self, s: str) -> bool: 
        # Sort the string and compare with the original
        return ("".join(sorted(list(s))) == s)


# Example usage
result = Solution().checkString("aaabbb")
print(result)  # Output: true
