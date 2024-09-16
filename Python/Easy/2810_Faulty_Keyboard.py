"""

Question: Faulty keyboard

Summary: Given a string 's', where typing the character ‘i’ reverses the string typed so far and other characters are typed normally,
return the final string that appears on the screen after typing all characters of 's'.

Method: Iterate through each character of the string, appending it to the result if it is not ‘i’.
If it is ‘i’, reverse the current result string.

Time complexity: O(n), where n is the length of the string.
Space complexity: O(n)
"""

class Solution:
    def finalString(self, s: str) -> str:
        result = ""

        # Iterate through each character of the string 
        for i in s:
            if i != "i":
                # Append the character to the result if it is not 'i'
                result += i
            else:
                # Reverse the result if the character is 'i'
                result = result[::-1]
              
        return result
                

# Example usage
result = Solution().finalString("string")
print(result)  # Output: "rtsng"
