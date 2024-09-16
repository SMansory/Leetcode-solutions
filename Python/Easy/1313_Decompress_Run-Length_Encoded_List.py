"""

Question: Decompress run-length encoded list

Summary: Given a list of integers 'nums' where each pair of elements '[freq, val]' represents the frequency and value respectively,
decompress the list by repeating 'val' 'freq' times. Return the decompressed list.

Method: Iterate through the list in steps of 2, extracting 'freq' and 'val' from each pair,
and extend the result list by repeating 'val' 'freq' times.

Time cmplexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        # Iterate through the list in steps of 2
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            # Extend the 'result' list by repeating 'val' 'freq' times
            result += [val] * freq
          
        return result


# Example usage
result = Solution().decompressRLElist([1, 2, 3, 4])
print(result)  # Output: [2, 4, 4, 4]
