"""

Question: Removing stars from a string

Summary: Given a string 's' containing stars (*),
remove each star and the closest non-star character to its left in one operation. 
Return the resulting string after all stars have been removed.

Method: Iterate through the string, use a stack to keep track of non-star characters, 
and remove the closest non-star character when a star is encountered.

Time complexity: O(n) - where 'n' is the length of the string.
Space complexity: O(n)
"""

class Solution:
    def removeStars(self, s: str) -> str:
        lst = []
      
        for i in s:
            if i != "*":
                lst.append(i)
            else:
                lst.pop()
              
        return "".join(lst)


# Example usage
result = Solution().removeStars("leet**cod*e")
print(result)  # Output: "lecoe"
