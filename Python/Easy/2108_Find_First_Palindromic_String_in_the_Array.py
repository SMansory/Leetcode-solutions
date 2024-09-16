"""

Question: Find first palindromic string in the array

Summary: Given an array of strings 'words', return the first palindromic string in the array.
If no such string exists, return an empty string. A string is  considered palindromic if it reads the same forward and backward.

Method: Iterate through the array and check each string to see if it is a palindrome. Return the first palindromic string found.

Time complexity: O(n * m), where n is the number of strings and m is the average length of the strings.
Space complexity: O(1)
"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate through the array of strings 
        for word in words:
            # Check if the string is a palindrome
            if word == word[::-1]:
                return word
        return ""


# Example usage
result = Solution().firstPalindrome(["abc", "car", "ada", "racecar", "cool"])
print(result)  # Output: "ada"
