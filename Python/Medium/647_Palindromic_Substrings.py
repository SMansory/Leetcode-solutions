"""

Question: Palindromic substrings 

Summary: Given a string 's', return the number of palindromic substrings in it. 
A string is a palindrome if it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Method: Iterate through all possible substrings of the string 's', check if each substring is a palindrome,
and count the number of palindromic substrings.

Time complexity: O(n^3) - where 'n' is the length of the string. 
Generating substrings takes O(n^2) and checking each substring for palindrome takes O(n).
Space complexity: O(n^2) - Space needed to store all substrings.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        arr = []
      
        for i in range(1, len(s) + 1):
            for j in range(i):
                substr = s[j:i]
                arr.append(substr)
              
        for k in arr:
            if k == k[::-1]:
                count += 1
              
        return count


# Example usage
result = Solution().countSubstrings("abc")
print(result)  # Output: 3
