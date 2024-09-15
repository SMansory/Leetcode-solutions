"""
Problem: Kids with the greatest number of candies

Question : Given an array 'candies' where 'candies[i]' represents the number of candies the ith kid has, and an integer 'extraCandies',
return a boolean array where each element indicates if the ith kid can have the greatest number of candies after receiving all 'extraCandies'.

Method: Use list comprehension to check if each kid's candies plus 'extraCandies' is greater than or equal to the maximum candies any kid currently has.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Check if each kid can have the greatest number of candies after receiving extraCandies
        return [True if i + extraCandies >= max(candies) else False for i in candies]


# Example usage
result = Solution().kidsWithCandies([2, 3, 5, 1, 3], 3)
print(result)  # Output: [true,true,true,false,true]
