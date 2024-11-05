"""

Question: Valid parantheses

Summary: Determine if a string containing '(', ')', '{', '}', '[' and ']' is valid. 
A valid string means brackets are correctly closed in order and 
each closing bracket matches its corresponding opening bracket.

Method: Check if each character is an opening bracket and add it to a stack.
If a closing bracket is encountered, check if it matches the last opened bracket in the stack. 
Return False if there's a mismatch or the stack is empty. Return True if the stack is empty after processing the string.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        arr = {'(':')', '{':'}','[':']'}
        stack = []
      
        for i in s:
          
            if i in arr:
                stack.append(i)
            elif len(stack) == 0 or arr[stack.pop()] != i:
                return False
              
        return len(stack) == 0


# Example usage
result = Solution().isValid("()")
print(result)  # Output: true
