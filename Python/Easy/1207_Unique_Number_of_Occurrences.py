"""

Question: Unique number of occurrences

Summary: Given an array of integers 'arr', determine if the number of occurrences of each value in the array is unique.
Return true if all occurrences are unique, otherwise return false.

Method: Use a Counter to count the occurrences of each value,
then check if the counts are unique by comparing the length of the list of counts to the length of the set of counts.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(sorted(arr))
        lst = [v for k, v in c.items()]
      
        if len(list(set(lst))) == len(lst):
            return True
        else:
            return False


# Example usage
result = Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3])
print(result)  # Output: true
