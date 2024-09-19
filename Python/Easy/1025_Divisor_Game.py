"""

Question: Divisor game

Summary: Alice and Bob take turns playing a game starting with a number 'n' on the chalkboard.
On each turn, a player chooses any 'x' such that '0 < x < n' and 'n % x == 0', then replaces 'n' with 'n - x'. 
The player who cannot make a move loses. Return true if Alice wins the game assuming both play optimally,
otherwise return false.

Method: Alice wins if the initial number 'n' is even, otherwise Bob wins.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def divisorGame(self, n: int) -> bool:
        # Alice wins if 'n' is even, otherwise Bob wins
        return True if n % 2 == 0 else False


# Example usage
result = Solution().divisorGame(2)
print(result)  # Output: true
