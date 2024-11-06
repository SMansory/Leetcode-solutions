"""

Question: Find all duplicates in an array

Summary: Given an integer array 'nums' of length 'n' where all the integers are in the range [1, n] and 
each integer appears at most twice, return an array of all the integers that appear twice. 
The solution should run in O(n) time and use only constant auxiliary space, excluding the space needed to store the output.

Method: Use a counter to count occurrences of each number and collect the ones that appear more than once.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [key for key, value in count.items() if value > 1]


# Example usage
result = Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
print(result)  # Output: [3, 2]
