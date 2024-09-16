"""

Question: Minimum average of smallest and largest elements

Summary: Given an array nums of 'n' integers (where 'n' is even), repeatedly remove the smallest and largest elements, 
compute their average, and add it to a list called 'averages'. Return the minimum value from the 'averages' list.

Method: Sort the array, then iteratively remove the smallest and largest elements, compute their average,
and store it in the 'averages' list. Finally, return the minimum value from the 'averages' list.

Time complexity: O(n log n).
Space complexity: O(n).
"""

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # Sort the array
        nums.sort()
      
        averages = []

        # Repeat the process until the array is empty
        while nums:
            # Remove the smallest and largest elements
            minElement = nums.pop(0)
            maxElement = nums.pop(-1)
            # Compute their average and append to the 'averages' list
            averages.append((minElement + maxElement) / 2)
          
        # Return the minimum value from the 'averages' list
        return min(averages)


# Example usage
result = Solution().minimumAverage([7, 8, 3, 4, 15, 13, 4, 1])
print(result)  # Output: 5.5
