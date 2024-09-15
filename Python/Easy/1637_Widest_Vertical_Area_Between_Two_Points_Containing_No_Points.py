"""
Question: Widest vertical area between two points 

Summary: Given 'n' points on a 2D plane where 'points[i] = [xi, yi]',
return the widest vertical area between two points such that no points are inside the area. 
A vertical area extends infinitely along the y-axis. The widest vertical area is the one with the maximum width. 

Method: Sort the points by their x-coordinates and find the maximum difference between consecutive x-coordinates.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Sort the points based on their x-coordinates
        points.sort(key = lambda x: x[0])

        # Initialize the result to stor the maximum width
        result = 0

        # Iterate through the sorted points to find the maximum width
        for i in range(1, len(points)):
            result = max(result, points[i][0] - points[i - 1][0])
          
        return result


# Example usage
result = Solution().maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])
print(result)  # Output: 1
