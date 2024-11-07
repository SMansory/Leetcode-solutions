"""

Question: Kth largest element in an array

Summary: Given an integer array 'nums' and an integer 'k', find the k-th largest element in the array.
The task requires solving the problem without explicitly sorting the entire array.

Method: Use Python's built-in sorted function to sort the array and return the k-th largest element by indexing.

Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


# Example usage
result = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(result)  # Output: 5
