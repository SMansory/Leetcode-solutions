"""

Question: Determine the maximum number of words in a sentence

Summary: Given an array of strings sentences, where each element represents a single sentence,
return the maximum number of words found in any single sentence. 
Each sentence is a list of words separated by a single space, with no leading or trailing spaces.

Method: Split each sentence into words and find the maximum length among these lists.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Split each sentence into words and return the maximum length
        return max(len(char.split()) for char in sentences)


# Example usage
result = Solution().mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print(result)  # Output: 6
