"""

Question: Nim game

Summary: Given a heap of stones, you and your friend take turns to remove 1 to 3 stones. You go first.
The player who removes the last stone wins. Determine if you can win the game, assuming both players play optimally.

Method: Use modulo operation to check if the number of stones is a multiple of 4. If it is, you lose; otherwise, you win.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return False if n % 4 == 0 else True


# Example usage
result = Solution().canWinNim(4)
print(result)  # Output: false
