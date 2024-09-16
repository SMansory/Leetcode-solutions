"""
Question: Count good pairs

Summary: Given two integer arrays 'nums1' and 'nums2' of lengths 'n' and 'm' respectively, 
and a positive integer 'k', return the total number of good pairs. 
A pair '(i, j)' is called good if 'nums1[i]' is divisible by 'nums2[j] * k' (0 <= i <= n - 1, 0 <= j <= m - 1).

Method: Use nested loops to check each pair and count the good pairs.

Time complexity: O(n * m)
Space complexity: O(1)
"""

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0

        # Iterate through each element in 'nums1'
        for i in range(len(nums1)):
            # Iterate through each element in 'nums2'
            for j in range(len(nums2)):
                # Check if 'nums[i]' is divisible by 'nums2[j] * k'
                if nums1[i] % (nums2[j] * k) == 0:
                    count += 1
                  
        return count


# Example usage
result = Solution().numberOfPairs([1, 3, 4], [1, 3, 4], 1)
print(result)  # Output: 5
