"""

Question: Max consecutive ones


Summary: You are given a binary array 'nums', return the maximum number of consecutive 1’s present in the array 'nums'.


Method: Iterate through the array, 
maintaining a count of consecutive 1’s and updating the maximum count whenever a 1 is encountered.
Reset the count when a 0 is encountered.


Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0

        for num in nums:

            if num == 1:
                count += 1
                maximum = max(maximum, count)

            else:
                count = 0

        return maximum


# Example usage
result = Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
print(result)  # Output: 3
