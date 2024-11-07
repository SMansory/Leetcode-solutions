"""

Question: Find peak element

Summary: Given a 0-indexed integer array 'nums', 
find a peak element (an element that is strictly greater than its neighbors) and return its index. 
If there are multiple peaks, return the index of any peak. The solution must run in O(log n) time complexity.

Method: The provided solution uses the 'max' function to find the peak element and 
then the 'index' function to find its position in the array.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))


# Example usage
result = Solution().findPeakElement([1, 2, 3, 1])
print(result)  # Output: 2
