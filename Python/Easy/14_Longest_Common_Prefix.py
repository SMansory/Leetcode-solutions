"""

Question: Longest common prefix

Summary: Write a function to find the longest common prefix string amongst an array of strings. 
If there is no common prefix, return an empty string "".

Method: Sort the array of strings. 
Compare the first and last strings character by character until a mismatch is found or until 
the end of the shorter string is reached. Accumulate the common characters to form the longest common prefix.

Time complexity: O(n log n) due to sorting
Space complexity: O(1)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        # Sort the array of strings
        strs = sorted(strs)
        # Compare the first and last strings
        first = strs[0]
        last = strs[-1]

        # Find the common prefix between the first and last strings
        for i in range(min(len(first), len(last))):

            if first[i] != last[i]:
                return result

            result += first[i]

        return result
        

# Example usage
result = Solution().longestCommonPrefix(["flower","flow","flight"])
print(result)  # Output: "fl"
