"""

Question: Check if a sentence is a pangram

Summary: A pangram is a sentence that contains every letter of the English alphabet at least once.
Given a string 'sentence' containing only lowercase English letters, return true if the sentence is a pangram, or false otherwise.

Method: Convert the sentence to a set of characters and check if the length of the set is 26,
which indicates that all letters of the alphabet are present.

Time complexity: O(n), where n is the length of the 'sentence'.
Space complexity: O(1)
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Check if the set of characters in sentence has 26 unique letters 
        return True if len(set(sentence)) == 26 else False


# Example usage
result = Solution().checkIfPangram("leetcode")
print(result)  # Output: false
