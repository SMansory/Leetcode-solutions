"""

Question: Sort array by parity II

Summary: Given an array of integers 'nums' where half of the integers are odd and the other half are even,
sort the array such that whenever 'nums[i]' is odd, 'i' is odd, and whenever 'nums[i]' is even, 'i' is even. 
Return any array that satisfies this condition.

Method: Separate the even and odd numbers into two lists,
then merge them back into the result list by alternating between even and odd numbers.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        arr = []

        # Separate even and odd numbers
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        # Merge even and odd numbers back into the result array
        for i in range(len(even)):
            arr.append(even[i])
            arr.append(odd[i])
          
        return arr


# Example usage
result = Solution().sortArrayByParityII([4, 2, 5, 7])
print(result)  # Output: [4, 5, 2, 7]
