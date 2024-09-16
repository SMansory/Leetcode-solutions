"""

Question: Count of matches in a tournament

Summary: Given an integer 'n' representing the number of teams in a tournament with specific rules,
return the total number of matches played until a winner is decided.
If the number of teams is even, each team is paired, and 'n / 2' matches are played.
If the number of teams is odd, one team advances randomly, and '(n - 1) / 2' matches are played.

Method: The total number of matches played in the tournament is always 'n - 1'.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def numberOfMatches(self, n: int) -> int:
        # The total number of matches is always 'n - 1'
        return n - 1


# Example usage
result = Solution().numberOfMatches(7)
print(result)  # Output: 6
