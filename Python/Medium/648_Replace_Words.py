"""

Question: Replace words

Summary: Replace all derivatives in a sentence with their corresponding roots from a given dictionary.
If multiple roots can replace a derivative, use the shortest root.

Method: Split the sentence into individual words. For each word, check if it starts with any of the roots in the dictionary.
If it does, and the root is shorter than the word, replace the word with the root. 
Join the modified words back into a sentence.

Time complexity: O(n * m) - where 'n' is the number of words in the sentence and 'm' is the number of roots in the dictionary.
Space complexity: O(n) - where 'n' is the length of the sentence due to storing the split words.
"""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
      
        for i in range(len(sentence)):
            s = sentence[i]

            for word in dictionary:
                if s.startswith(word):
                    if len(word) < len(s):
                        s = word

            sentence[i] = s
          
        return " ".join(sentence)


# Example usage
result = Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
print(result)  # Output: "the cat was rat by the bat"
