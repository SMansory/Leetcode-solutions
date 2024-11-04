"""

Question: Contains duplicate II

Summary: Given an integer array 'nums' and an integer 'k', 
return true if there are two distinct indices 'i' and 'j' such that nums[i] == nums[j] and 
the absolute difference between 'i' and 'j' is less than or equal to 'k'.

Method: Check if the array has duplicates by comparing its length to the length of its set version. 
If duplicates exist, iterate through the array with nested loops to find indices 'i' and 'j' that meet the condition.

Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if abs(i - j) <= k:
                        return True

        return False


# Example usage
result = Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)
print(result)  # Output: true
