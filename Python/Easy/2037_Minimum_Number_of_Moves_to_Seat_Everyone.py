"""
Question: Minimum Number of Moves to Seat Everyone

Summary: Given arrays 'seats' and 'students' of length 'n', 
where 'seats[i]' is the position of the ith seat and 'students[j]' is the position of the jth student, 
return the minimum number of moves required to seat each student such that no two students are in the same seat.
Moves involve increasing or decreasing the position of a student by 1.

Method: Sort both arrays and calculate the sum of absolute differences between corresponding elements.

Time complexity: O(n log n)
Space complexity: O(1)
"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both seats and students arrays
        seats.sort()
        students.sort() 

        # Initialize the count of moves
        count = 0

        # Calculate the sum of absolute differences between corresponding elements
        for i in range(len(students)):
            count += abs(seats[i] - students[i])
          
        return count


# Example usage
result = Solution().minMovesToSeat([3, 1, 5], [2, 7, 4])
print(result)  # Output: 4
