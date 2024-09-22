"""

Question: Rotate string 


Summary: Given two strings 's' and 'goal', 
return true if 's' can be transformed into 'goal' by performing a series of shifts.
A shift involves moving the leftmost character of 's' to the rightmost position.


Method: Check if the length of 's' is equal to the length of 'goal' and 
if 's' is a substring of 'goal' concatenated with itself.


Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if lengths are equal and if 's' is a substring of 'goal' concatenated with itself
        return ((len(s) == len(goal)) and (s in goal + goal))


# Example usage
result = Solution().rotateString("abcde", "cdeab")
print(result)  # Output:  true
