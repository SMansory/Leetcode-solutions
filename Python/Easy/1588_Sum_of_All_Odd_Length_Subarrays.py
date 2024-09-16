"""

Question: Sum of all odd-length subarrays

Summary: Given an array of positive integers 'arr', return the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.

Method: Iterate through the array, generating all possible odd-length subarrays, and sum their elements.

Time complexity: O(n^3), where n is the length of the array.
Space complexity: O(1)
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_sum = 0

        # Iterate through the array to generate subarrays
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                # Sum the elements of each odd-length subarray
                odd_sum += sum(arr[i: j + 1])
              
        return odd_sum


# Example usage
result = Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3])
print(result)  # Output: 58
