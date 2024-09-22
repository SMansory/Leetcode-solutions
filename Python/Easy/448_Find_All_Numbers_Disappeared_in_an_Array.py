"""

Question: Find all numbers disappeared in an array


Summary: You are given an array 'nums' of 'n' integers where 'nums[i]' is in the range '[1, n]', 
return an array of all the integers in the range '[1, n]' that do not appear in nums.


Method: Use sets to find the difference between the complete range of numbers and the numbers present in the array.


Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Create a set of all numbers from 1 to 'n'
        set1 = set(range(1, len(nums) + 1))
        # Create a set of numbers present in the array
        set2 = set(nums)
        # Return the difference between the two sets as a list
        return list(set1 - set2)


# Example usage
result = Solution().findDisappearedNumbers([1, 1])
print(result)  # Output: [2]
