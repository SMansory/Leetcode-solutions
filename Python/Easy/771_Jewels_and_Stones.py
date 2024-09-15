"""
Problem: Count jewels in stones
Summary: Given strings 'jewels' and 'stones', count how many stones are also jewels. The comparison is case-sensitive.
Method: Use nested loops to compare each stone with each jewel.
Time complexity: O(n * m), where n is the length of stones and m is the length of jewels.
Space complexity: O(1)
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Convert jewels and stones strings to lists
        jewel = list(jewels)
        stone = list(stones)
      
        count = 0

        # Iterate through each jewel and stone to count matches
        for j in jewel:
            for s in stone:
                if j == s:
                    count += 1
                  
        return count


# Example usage
result = Solution().numJewelsInStones("aA", "aAAbbbb")
print(result)  # Output: 3
