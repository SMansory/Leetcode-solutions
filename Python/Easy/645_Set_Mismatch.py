"""

Question: Set mismatch

Summary: Given an integer array 'nums' representing a set of integers from 1 to 'n' with one duplicated number and 
one missing number, find and return the duplicated number and the missing number in the form of an array.

Method: Use a counter to count occurrences of each number in the array. Identify the number that occurs twice. 
Calculate the missing number using the difference between the expected sum of numbers from 1 to 'n' and 
the actual sum of the array.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
      
        for i, j in count.items():
            if j == 2:
                res = i
              
        res1 = (n * (n + 1)) // 2 - (sum(nums) - res)
        return [res, res1]


# Example usage
result = Solution().findErrorNums([1, 1])
print(result)  # Output: [1, 2]
