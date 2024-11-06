"""

Question: Find and replace pattern

Summary: Given a list of strings 'words' and a string 'pattern', return a list of words that match the 'pattern'. 
A word matches the pattern if there exists a permutation of letters such that replacing each letter in the 'pattern' with 
the corresponding letter in the word results in the desired word. The solution should be returned in any order.

Method: Check each word in 'words' to see if it matches the 'pattern' by comparing the sets of zipped pairs and 
ensuring they match the sets of the word and the pattern.

Time complexity: O(n * m) - where 'n' is the number of words and 'm' is the length of the longest word.
Space complexity: O(n + m) - considering the space needed to store the sets.
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [i for i in words if len(set(zip(i, pattern))) == len(set(i)) == len(set(pattern))]


# Example usage
result = Solution().findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")
print(result)  # Output: ["mee", "aqq"]
