"""

Question: Number of arithmetic triplets

Summary: Given a 0-indexed, strictly increasing integer array 'nums' and a positive integer 'diff',
return the number of unique arithmetic triplets.
A triplet ((i, j, k)) is an arithmetic triplet if (i < j < k), (nums[j] - nums[i] = diff), and (nums[k] - nums[j] = diff).

Method: Use three nested loops to iterate through all possible triplets and count those that satisfy the conditions.

Time complexity: O(n^3), where n is the length of the array.
Space complexity: O(1)
"""

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        # Iterate through all possible triplets
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    # Check if the triplet satisfies the conditions
                    if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                        count += 1
                      
        return count


# Example usage
result = Solution().arithmeticTriplets([0, 1, 4, 6, 7, 10], 3)
print(result)  # Output: 2
