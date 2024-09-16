"""
Question: Truncate a sentence

Summary: Given a sentence 's' consisting of words separated by single spaces, and an integer 'k', 
truncate the sentence so that it contains only the first 'k' words. Return the truncated sentence.

Method: Split the sentence into words, select the first 'k' words, and join them back into a string.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Split the sentence into words
        ans = s.split()
        # Select the first 'k' words
        ans1 = ans[0 : k]
        # Join the selected words back into a string
        result = " ".join(ans1)
        return result


# Example usage
result = Solution().truncateSentence("Hello how are you Contestant", 4)
print(result)  # Output: "Hello how are you"
