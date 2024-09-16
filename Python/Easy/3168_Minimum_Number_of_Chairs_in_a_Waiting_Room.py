"""

Question: Minimum number of chairs in a waiting room

Summary: Given a string 's' where each character represents an event at each second:
1. ‘E’ means a person enters the waiting room and takes a chair.
2. ‘L’ means a person leaves the waiting room, freeing up a chair. 
Return the minimum number of chairs needed to ensure a chair is available for every person who enters the waiting room, 
starting from an initially empty room.

Method: Iterate through the string, keeping track of the current number of occupied chairs and 
updating the maximum number of chairs needed.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        result = 0
      
        for i in s:
            if i == "E":
                count += 1
            elif i == "L":
                count -= 1
            result = max(count, result)
          
        return result


# Example usage
result = Solution().minimumChairs("EEEEEEE")
print(result)  # Output: 7
