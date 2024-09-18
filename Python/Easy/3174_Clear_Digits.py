"""

Question: Clear digits

Summary: Given a string 's', 
repeatedly remove the first digit and the closest non-digit character to its left until all digits are removed. 
Return the resulting string after all operations.

Method: Use a stack to keep track of non-digit characters. For each digit encountered, 
pop the last non-digit character from the stack. 
Finally, join the remaining characters in the stack to form the resulting string.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def clearDigits(self, s: str) -> str:
        arr = []
      
        for i in s:
            if i.isdigit():
                # Remove the closest non-digit character to the left
                arr.pop()
            else:
                # Add non-digit characters to the stack
                arr.append(i)
              
        return "".join(arr) 


# Example usage
result = Solution().clearDigits("abc")
print(result)  # Output: "abc"
