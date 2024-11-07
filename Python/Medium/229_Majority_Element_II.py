"""

Question: Majority element II

Summary: Find all elements in an integer array 'nums' of size 'n' that appear more than '⌊ n/3 ⌋' times.

Method: Iterate through the array and count the occurrences of each element. 
Append elements that appear more than '⌊ n/3 ⌋' times to a result list, 
and ensure uniqueness by converting the list to a set and back to a list.

Time complexity: O(n^2) - Due to the count method within the loop.
Space complexity: O(n)
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr = []
      
        for i in nums:
            if nums.count(i) > len(nums) / 3:
                arr.append(i)
              
        return list(set(arr))


# Example usage
result = Solution().majorityElement([3, 2, 3])
print(result)  # Output: [3]
