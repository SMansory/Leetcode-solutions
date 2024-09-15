"""
Problem: Number of employees who met the target

Summary: Given an array 'hours' where 'hours[i]' represents the hours worked by the ith employee, and an integer 'target', 
return the number of employees who worked at least 'target' hours.

Method: Use a list comprehension to count the number of employees who meet or exceed the target hours.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # Count the number of employees who worked at least target hours
        count = len([i for i in hours if i >= target])
      
        return count


# Example usage
result = Solution().numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2)
print(result)  # Output: 3
