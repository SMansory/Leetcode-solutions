"""

Question: Find the difference


Summary: Given two strings 's' and 't', 
where 't' is generated by shuffling 's' and adding one extra letter at a random position, 
return the extra letter that was added to 't'.


Method: Convert both strings to lists, sort them, and compare them element by element to find the extra letter.


Time complexity: O(n log n) due to sorting
Space complexity: O(n) for storing the lists
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Convert strings to lists
        s = list(s)
        t = list(t)

        # Sort the lists     
        s.sort()
        t.sort()

        # Append an empty string to handle the extra character
        s.append("")

        # Compare elements to find the extra character
        for i in range(len(t)):
            if s[i] != t[i]:
                return t[i]


# Example usage
result = Solution().findTheDifference("", "y")
print(result)  # Output: "y"
