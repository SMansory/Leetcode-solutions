"""

Question: Reverse words in a string III

Summary: Given a string 's',
reverse the order of characters in each word within the sentence while preserving the whitespace and the initial word order.

Method: Split the sentence into words, reverse each word, and join them back into a sentence.

Time complexity: O(n), where n is the length of the string.
Space complexity: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the sentence into words
        ans = s.split()
        # Reverse each word
        result = map(lambda word: word[::-1], ans)
        # Join the reversed words into a sentence
        return " ".join(result) 


# Example usage
result = Solution().reverseWords("Let's take LeetCode contest")
print(result)  # Output: "s'teL ekat edoCteeL tsetnoc"
