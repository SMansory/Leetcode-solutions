"""

Question: Shuffle string

Summary: Given a string 's' and an integer array indices of the same length, 
shuffle the string such that the character at the i-th position moves to 'indices[i]' in the shuffled string. 
Return the shuffled string.

Method: Create an empty list of the same length as the string, 
place each character at its new position according to the indices array, and join the list into a string.

Time complexity: O(n), where n is the length of the string.
Space complexity: O(n)
"""

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create an empty list of the same length as the string
        ans = [0] * len(s)
      
        # Place each character at its new position
        for i in range(len(s)):
            ans[indices[i]] = s[i]

        # Join the list into a string 
        result = "".join(ans)
      
        return result


# Example usage
result = Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3])
print(result)  # Output: "leetcode"
