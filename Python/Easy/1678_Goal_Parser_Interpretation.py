"""
Question: Goal parser interpretation

Summary: Given a string `command` consisting of "G", "()", and/or "(al)", 
return the interpreted string where "G" is interpreted as "G", "()" as "o", and "(al)" as "al".

Method: Use string replacement to interpret the command.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def interpret(self, command: str) -> str:
        # Replace "()" with "o"
        result = command.replace("()", "o")
        # Replace "(al)" with "al"
        return result.replace("(al)", "al") 


# Example usage
result = Solution().interpret("G()(al)")
print(result)  # Output: "Goal"
