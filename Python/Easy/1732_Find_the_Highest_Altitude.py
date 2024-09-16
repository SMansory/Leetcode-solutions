"""

Question: Find the highest altitude

Summary: A biker starts a road trip at point 0 with an altitude of 0. Given an integer array 'gain' of length 'n',
where 'gain[i]' represents the net gain in altitude between points 'i' and 'i + 1', return the highest altitude reached during the trip.

Method: Initialize the altitude at 0 and iterate through the 'gain' array, 
updating the current altitude and keeping track of the highest altitude reached.

Time complexity: O(n), where n is the length of the 'gain' array.
Space complexity: O(n)
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Initialize the 'altitude' list with the starting point
        altitude = [0]
        result = 0
      
        # Iterate through the 'gain' array to calculate altitudes
        for i in gain:
            result += i
            altitude.append(result)

        # Return the heighest altitude reached
        return max(altitude)


# Example usage
result = Solution().largestAltitude([-5, 1, 5, 0, -7])
print(result)  # Output: 1
