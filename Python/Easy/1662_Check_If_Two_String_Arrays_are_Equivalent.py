"""

Question: Check if two string arrays are equivalent

Summary: Given two string arrays 'word1' and 'word2',
return 'true' if the two arrays represent the same string when their elements are concatenated in order, and 'false' otherwise.

Method: Concatenate the elements of each array into a single string and compare the resulting strings.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Concatenate the elements of each array into a single string
        word1 = ''.join(str(i) for i in word1)
        word2 = ''.join(str(j) for j in word2)

        # Compare the resulting strings
        if word1 == word2:
            return True
        else:
            return False


# Example usage
result = Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
print(result)  # Output: true
