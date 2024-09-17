"""

Question: Find the peaks

Summary: Given a 0-indexed array 'mountain', find all the peaks in the array. 
A peak is an element that is strictly greater than its neighboring elements. 
The first and last elements of the array are not considered peaks. Return an array of indices of the peaks in any order.

Method: Iterate through the array from the second element to the second-to-last element,
checking if each element is greater than its neighbors.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        result = []
      
        for i in range(1, len(mountain) - 1):
            # Check if the current element is greater than its neighbors
            if (mountain[i] > mountain[i - 1]) and (mountain[i] > mountain[i + 1]):
                result.append(i)
              
        return result


# Example usage
result = Solution().findPeaks([2, 4, 4])
print(result)  # Output: []
