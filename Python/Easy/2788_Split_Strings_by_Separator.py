"""

Question: Split strings by separator

Summary: Given an array of strings 'words' and a character 'separator', split each string in 'words' by the 'separator'. 
Return an array of strings containing the new strings formed after the splits, excluding empty strings. 
The resulting strings must maintain the same order as they were initially given.

Method: Iterate through each string in the array, split it by the 'separator', and collect the non-empty resulting strings.

Time complexity: O(n * m) (where 'n' is the number of strings and 'm' is the average length of the strings)
Space complexity: O(n * m)
"""

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
      
        for i in words:
            # Split each string by the 'seperator'
            word = i.split(separator)
            # Collect non-empty resulting strings
            for j in word:
                if j:
                    result.append(j)
                  
        return result


# Example usage
result = Solution().splitWordsBySeparator(["one.two.three", "four.five", "six"], ".")
print(result)  # Output: ["one","two","three","four","five","six"]
