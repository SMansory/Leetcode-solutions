"""

Question: Greatest english letter in upper and lower case

Summary: Given a string 's' of English letters, 
return the greatest English letter that appears in both lowercase and uppercase in 's'.
The returned letter should be in uppercase. If no such letter exists, return an empty string.
A letter 'b' is greater than another letter 'a' if 'b' appears after 'a' in the English alphabet.

Method: Iterate through the alphabet, 
checking if both the lowercase and uppercase versions of each letter are present in the string. 
Collect these letters, sort them in descending order, and return the greatest one.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        arr = [""]
      
        for i in letters:
            # Check if both lowercase and uppercase versions are in the string
            if i in s and i.upper() in s:
                arr.append(i.upper())

        # Sort the collected letters in descending order and return the greatest one
        arr = sorted(arr, reverse=True)
      
        return arr[0]


# Example usage
result = Solution().greatestLetter("lEeTcOdE")
print(result)  # Output: "E"
