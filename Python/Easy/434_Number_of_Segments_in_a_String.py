"""

Question: Number of segments in a string

Summary: Given a string 's', return the number of segments in the string.
A segment is defined as a contiguous sequence of non-space characters.

Method: Use the split() method to break the string into segments based on spaces and return the length of the resulting list.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


# Example usage
result = Solution().countSegments("Hello, my name is John")
print(result)  # Output: 5
