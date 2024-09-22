"""

Question: Majority element

Summary: You are given an array nums of size 'n', return the majority element.
The majority element is the element that appears more than '⌊n / 2⌋' times. 

Method: Use a counter to count the frequency of each element and return the element with the highest frequency.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)  # Count the frequency of each element
        return max(count, key=count.get)  # Return the element with the highest frequency


# Example usage
result = Solution().majorityElement([3, 2, 3])
print(result)  # Output: 3
