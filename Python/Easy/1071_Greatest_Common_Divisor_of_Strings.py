"""

Question: Greatest common divisor of strings

Summary: Given two strings 'str1' and 'str2', return the largest string 'x' such that 'x' divides both 'str1' and 'str2'. 
A string 't' divides 's' if 's' can be constructed by concatenating 't' multiple times.

Method: Check if the concatenation of 'str1' and 'str2' equals the concatenation of 'str2' and 'str1'. 
If true, return the substring of 'str1' up to the greatest common divisor (GCD) of their lengths.

Time complexity: O(n + m)
Space complexity: O(1)
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenations of 'str1' and 'str2' in both orders are equal
        if str1 + str2 != str2 + str1:
            return "" 
        # Return the substring of 'str1' up to the GCD of lengths of 'str1' and 'str2'  
        return str1[:gcd(len(str1), len(str2))]


# Example usage
result = Solution().gcdOfStrings("ABCABC", "ABC")
print(result)  # Output: "ABC"
