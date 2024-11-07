"""

Question: Top k frequent elements

Summary: Given an integer array 'nums' and an integer 'k', return the 'k' most frequent elements. 
The answer can be returned in any order.

Method: Use a counter to count the frequency of each element in the array.
Then, use the 'most_common' method of the counter to get the 'k' most frequent elements.

Time complexity: O(n log k)
Space complexity: O(n)
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [i[0] for i in count.most_common(k)]


# Example usage
result = Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(result)  # Output: [1, 2]
