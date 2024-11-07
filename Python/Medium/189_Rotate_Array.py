"""

Question: Rotate array

Summary: Rotate an integer array 'nums' to the right by 'k' steps, where 'k' is non-negative.

Method: Use a loop to pop the last element of the array and insert it at the beginning, repeating this process 'k' times.

Time complexity: O(n * k) - Iterating 'k' times over the array.
Space complexity: O(1)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            pop = nums.pop()
            nums.insert(0, pop)


# Example usage
result = Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
print(result)  # Output: [5, 6, 7, 1, 2, 3, 4]
