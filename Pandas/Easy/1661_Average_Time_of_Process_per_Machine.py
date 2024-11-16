"""

Question: Average time of process per machine

Summary: Write a function to find the average time each machine takes to complete a process. 
The average time is calculated by the total time to complete every process on the machine 
divided by the number of processes that were run. The resulting table should have the 'machine_id' along with the
average time as 'processing_time', which should be rounded to 3 decimal places.

Method: Pivot the activity DataFrame to arrange start and end timestamps in separate columns. 
Calculate the processing time by subtracting start from end. Group by 'machine_id' and 
calculate the mean of the processing times, rounding the result to 3 decimal places.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # Pivot the table to separate start and end timestamps
    result = activity.pivot(index = ["machine_id", "process_id"], columns = "activity_type", values = "timestamp")
    # Calculate processing time
    result["processing_time"] = result["end"] - result["start"]
    # Group by 'machine_id' and calculate the average processing time
    return result.groupby("machine_id").processing_time.mean().round(3).reset_index()


# Example usage
data = {
    'machine_id': [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2],
    'process_id': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    'activity_type': ['start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end', 'start', 'end'],
    'timestamp': [0.712, 1.52, 3.14, 4.12, 0.55, 1.55, 0.43, 1.42, 4.1, 4.512, 2.5, 5.0]
}
activity = pd.DataFrame(data)

result = get_average_time(activity)
print(result)
