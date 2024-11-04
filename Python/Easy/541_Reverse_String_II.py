"""

Question: Reverse string II

Summary: You are given a string 's' and an integer 'k', 
reverse the first 'k' characters for every 2k characters from the start of the string.
If fewer than 'k' characters remain, reverse all of them. 
If fewer than 2k but at least 'k' characters remain, reverse the first 'k' and leave the rest as they are.

Method: Split the string into chunks of 'k' characters, reverse every other chunk, and then join the chunks back together.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
      
        while s:
            # Append chunks of 'k' characters
            temp.append(s[:k])
            s = s[k:]

        # Reverse every other chunk
        for i in range(0, len(temp), 2):
            temp[i] = temp[i][::-1]

        # Join the chunks back together
        return ''.join(temp) 


# Example usage
result = Solution().reverseStr("abcdefg", 2)
print(result)  # Output: "bacdfeg"
