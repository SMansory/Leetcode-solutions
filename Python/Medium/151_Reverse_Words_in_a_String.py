"""

Question: Reverse words in a string

Summary: Given an input string 's', reverse the order of the words. A word is a sequence of non-space characters, 
separated by at least one space. Return the words in reverse order, concatenated by a single space. 
The returned string should not include leading, trailing, or multiple spaces between words.

Method: Strip leading and trailing spaces from the string, split the string by spaces to get the words, 
reverse the list of words, and join them with a single space.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.strip().split()))


# Example usage
result = Solution().reverseWords("the sky is blue")
print(result)  # Output: "blue is sky the"
