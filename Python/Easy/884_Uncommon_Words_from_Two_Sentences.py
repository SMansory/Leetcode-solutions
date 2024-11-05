"""

Question: Uncommon words from two sentences

Summary: Given two sentences 's1' and 's2', return a list of all the uncommon words. 
A word is uncommon if it appears exactly once in one of the sentences and does not appear in the other sentence.

Method: Split both sentences into words, combine the words, and iterate through the combined list. 
If a word appears exactly once, add it to the result list.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split both sentences into words
        s11 = s1.split()
        s22 = s2.split()
        # Combine the words from both sentences
        s11.extend(s22)
      
        arr = []
      
        # Iterate through the combined list to find uncommon words
        for i in s11:
          
            if s11.count(i) == 1:
                arr.append(i)
              
        return arr


# Example usage
result = Solution().uncommonFromSentences("this apple is sweet", "this apple is sour")
print(result)  # Output: ["sweet", "sour"]
