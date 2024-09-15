"""
Problem: Shuffle the array
Summary: Given an array 'nums' of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn], return the array in the form [x1,y1,x2,y2,...,xn,yn].
Method: Iterate through the first half of the array and interleave elements from the first and second halves.
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Initialize the arr list
        arr = []

        # Iterate through the first half of the array
        for i in range(0, n):
            # Append the element from the first half
            arr.append(nums[i])
            # Append the corresponding element from the second half
            arr.append(nums[i + n])
          
        return arr


# Example usage
result = Solution().shuffle([2, 5, 1, 3, 4, 7], 3)
print(result)  # Output: [2, 3, 5, 4, 1, 7]
