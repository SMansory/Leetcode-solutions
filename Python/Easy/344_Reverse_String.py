"""

Question: Reverse string

Summary: Write a function to reverse a string given as an array of characters 's'. 
The reversal must be done in-place with O(1) extra memory.

Method: Use slicing to reverse the array in-place.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        return s


# Example usage
result = Solution().reverseString(["h", "e", "l", "l", "o"])
print(result)  # Output: ["o", "l", "l", "e", "h"]
