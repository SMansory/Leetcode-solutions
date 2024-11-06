"""

Question: Sort characters by frequency

Summary: Given a string 's', sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Method: Use a counter to count the frequency of each character in the string. 
Sort the characters by frequency in descending order and 
construct the resulting string by repeating each character according to its frequency.

Time complexity: O(n log n) - where 'n' is the length of the string.
Space complexity: O(n)
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([key * value for key, value in sorted(Counter(s).items(), key=lambda x:x[1], reverse=True)])


# Example usage
result = Solution().frequencySort("tree")
print(result)  # Output: "eetr"
