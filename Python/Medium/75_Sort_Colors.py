"""

Question: Sort colors

Summary: Given an array 'nums' with 'n' objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent in the order red, white, and blue, 
represented by integers 0, 1, and 2 respectively. You must solve this problem without using the library's sort function.

Method: Implement a simple sorting algorithm to compare and swap elements in the array to ensure they are sorted in the desired order.

Time complexity: O(n^2) - Due to the nested loops used for comparing and swapping elements.
Space complexity: O(1)
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


# Example usage
result = Solution().sortColors([2, 0, 1])
print(result)  # Output: [0, 1, 2]
