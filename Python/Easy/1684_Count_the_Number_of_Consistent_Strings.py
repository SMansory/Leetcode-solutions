"""
Problem: Count consistent strings
Summary: Given a string 'allowed' consisting of distinct characters and an array of strings 'words', return the number of consistent strings in the array.
A string is consistent if all its characters appear in 'allowed'.
Method: Use a set to check if each word's characters are a subset of 'allowed'.
Time complexity: O(n * m), where n is the number of words and m is the average length of the words.
Space complexity: O(1)
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Initialize the count of consistent strings
        count = 0

        # Iterate through each word in the list
        for i in words:
            # Check if all characters in the word are in the allowed set
            if set(i).issubset(list(allowed)):
                count += 1
              
        return count


# Example usage
result = Solution().countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])
print(result)  # Output: 2
