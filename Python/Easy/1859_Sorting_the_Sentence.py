"""

Question: Sorting the sentence 

Summary: Given a shuffled sentence 's' where each word has a 1-indexed position appended to it,
reconstruct and return the original sentence. The sentence contains no more than 9 words, 
each separated by a single space with no leading or trailing spaces.

Method: Reverse the string and split it into words, sort the words based on their appended indices, 
remove the indices, and join the words back into a sentence.

Time complexity: O(n log n), where n is the number of words.
Space complexity: O(n)
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        # Reverse the string and split it into words
        arr = s[::-1].split()
        # Sort the word based on their append indices
        arr.sort()
        result = []

        # Remove the indices and reverse the words back
        for i in arr:
            result.append(i[1:][::-1])

        # Join the words back into a sentence 
        return " ".join(result)


# Example usage
result = Solution().sortSentence("is2 sentence4 This1 a3")
print(result)  # Output: "This is a sentence"
