"""

Question: Number of students doing homework at a given time

Summary: Given two integer arrays 'startTime' and 'endTime', and an integer 'queryTime',
determine the number of students who are doing their homework at 'queryTime'. 
Each student starts their homework at 'startTime[i]' and finishes at 'endTime[i]'.
Return the count of students for whom 'queryTime' falls within the interval '[startTime[i], endTime[i]]' inclusive.

Method: Iterate through the arrays and count the number of students whose 'queryTime' falls within their start and end times.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
      
        for i in range(len(startTime)):
            # Check if 'queryTime' is within the interval '[startTime[i], endTime[i]]'
            if queryTime >= startTime[i] and endTime[i] >= queryTime:
                count += 1
              
        return count


# Example usage
result = Solution().busyStudent([1, 2, 3], [3, 2, 7], 4)
print(result)  # Output: 1
