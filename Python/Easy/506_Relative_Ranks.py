"""

Question: Relative ranks 

Summary: Given an integer array 'score' where each element represents the score of an athlete in a competition,
return an array of ranks. The highest score gets “Gold Medal”, 
the second highest gets “Silver Medal”, the third highest gets “Bronze Medal”,
and the rest get their respective ranks as strings.

Method: Sort the scores in descending order and assign ranks based on their positions.
Use a dictionary to map scores to their ranks and then construct the result array based on the original scores.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        arr = []

        # Sort scores in descending order
        scores = sorted(score, reverse = True) 

        # Assign ranks based on sorted scores
        for i in range(len(scores)):
            if i == 0:
                d[scores[i]] = "Gold Medal"
            elif i == 1:
                d[scores[i]] = "Silver Medal"
            elif i == 2:
                d[scores[i]] = "Bronze Medal"
            else:
                d[scores[i]] = str(i + 1)

        # Construct the result array based on the original scores
        for i in range(len(score)):
            arr.append(d[score[i]])
          
        return arr


# Example usage
result = Solution().findRelativeRanks([5, 4, 3, 2, 1])
print(result)  # Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
