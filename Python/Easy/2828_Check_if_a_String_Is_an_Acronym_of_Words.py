"""

Question: Check if a string is an Acronym of Words

Summary: Given an array of strings 'words' and a string 's', check if 's' is an acronym of words. 
A string 's' is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order.
Return true if 's' is an acronym of words, and false otherwise.

Method: Concatenate the first character of each word in the array and compare the resulting string with 's'.

Time complexity: O(n), where n is the number of words.
Space complexity: O(n)
"""

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # Concatenate the first character of each word
        result = "".join([char[0] for char in words])

        # Check if the resulting string matches 's'
        if result == s:
            return True
        return False


# Example usage
result = Solution().isAcronym(["alice", "bob", "charlie"], "abc")
print(result)  # Output: true
