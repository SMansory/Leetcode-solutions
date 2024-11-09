"""

Question: Find total time spent by each employee

Summary: Write a function to calculate the total time in minutes spent by each employee on each day at the office. 
Note that within one day, an employee can enter and leave more than once.
The time spent in the office for a single entry is 'out_time' - 'in_time'.

Method: Calculate the time spent for each entry by subtracting 'in_time' from 'out_time',
then group by 'emp_id' and 'event_day' to sum the total time for each employee on each day. 
Rename the 'event_day' column to day.

Time complexity: O(n) 
Space complexity: O(1)
"""

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # Calculate time spent for each entry
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    # Group by employee and day, then sum the total time
    result = employees.groupby(["emp_id", "event_day"])["total_time"].sum().reset_index()
    # Rename column for clarity
    result.rename(columns = {"event_day": "day"}, inplace = True)
    return result


# Example usage
data = {'emp_id': [1, 1, 1, 2, 2], 'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'], 'in_time': [4, 55, 1, 3, 47], 'out_time': [32, 200, 42, 33, 74]} 
employees = pd.DataFrame(data) 

result = total_time(employees) 
print(result)
