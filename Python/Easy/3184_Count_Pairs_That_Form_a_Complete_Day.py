"""

Question: Count pairs that form a complete day I

Summary: Given an integer array 'hours' representing times in hours, 
return the number of pairs '((i, j))' where '(i < j)' and the sum of 'hours[i]' and 'hours[j]' is a multiple of 24.
A complete day is defined as a time duration that is an exact multiple of 24 hours.

Method: Use nested loops to iterate through all possible pairs of indices and count those whose sum is a multiple of 24.

Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
      
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    count += 1
                  
        return count


# Example usage 
result = Solution().countCompleteDayPairs([12, 12, 30, 24, 24])
print(result)  # Output: 2
