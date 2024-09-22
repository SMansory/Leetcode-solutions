"""

Question: Sort even and odd indices independently


Summary: Given a 0-indexed integer array 'nums', rearrange the values according to the following rules:

1. Sort the values at odd indices in non-increasing order.
2. Sort the values at even indices in non-decreasing order. Return the array formed after rearranging the values of 'nums'.


Method: Separate the values at odd and even indices, sort them accordingly, and then merge them back into a single array.


Time complexity: O(n log n)
Space complexity: O(n)
"""

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Separate the values at even and odd indices
        even = [nums[i] for i in range(len(nums)) if i % 2 == 0]
        odd = [nums[i] for i in range(len(nums)) if i % 2 != 0]

        # Sort even indices in non-decreasing order
        even.sort()
        # Sort odd indices in non-increasing order
        odd.sort(reverse=True)

        # Merge the sorted values back into a single array
        arr = []

        for i in range(len(even)):
            arr.append(even[i])
          
            if len(odd) > i:
                arr.append(odd[i])

        return arr


# Example usage
result  = Solution().sortEvenOdd([4, 1, 2, 3])
print(result)  # Output: [2, 3, 4, 1]
