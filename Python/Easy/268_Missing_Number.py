"""

Question: Missing number

Summary: Given an array 'nums' that includes 'n' distinct numbers in the range '[0, n]',
return the only number in the range that is missing from the array.

Method: Sort the array and iterate through it to find the missing number by comparing the index with the value at that index.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sort the array
        nums = sorted(nums)
      
        for i in range(0, len(nums)):
            # Check if the current index matches the value at that index
            if i != nums[i]:
                return i

        # If no mismatch is found, the missing number is 'n'
        return len(nums)


# Example usage
result = Solution().missingNumber([3, 0, 1])
print(result)  # Output: 2
