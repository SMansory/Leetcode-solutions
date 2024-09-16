"""

Question: Find maximum number of string pairs

Summary: Given a 0-indexed array 'words' consisting of distinct strings, 
return the maximum number of pairs that can be formed where 'words[i]' is equal to the reversed string of 'words[j]'
and (0 <= i < j < words.length). Each string can belong to at most one pair.

Method: Use nested loops to iterate through the array and count the pairs where one string is the reverse of another.

Time complexity: O(n^2), where n is the length of the array.
Space complexity: O(1)
"""

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0

        # Iterate through the array to find pairs
        for i in range(len(words)):
            for j in range(len(words)):
                # Check if 'words[i]' is the reverse of 'words[j]' and 'i < j'
                if (words[i] == words[j][::-1]) and (0 <= i < j < len(words)):
                    count += 1
                  
        return count


# Example usage
result = Solution().maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"])
print(result)  # Output: 2
