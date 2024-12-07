"""

Question: Exchange seats

Summary: Write a function that swaps the seat IDs of every two consecutive students. If the number of students is odd,
the last student's ID remains unchanged. The result should be ordered by 'id' in ascending order.

Method: Apply a lambda function to modify the 'id' column: increment the ID by 1 if it is odd (and not the last student),
or decrement by 1 if it is even. The DataFrame is then sorted by the 'id' column.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    # Apply a lambda function to swap seat IDs
    seat["id"] = seat["id"].apply(lambda x: x + 1 if x % 2 == 1 and x != len(seat) else x - 1 if x % 2 == 0 else x )
    # Sort the DataFrame by 'id'
    return seat.sort_values("id")


# Example usage
seat_data = {
    'id': [1, 2, 3, 4, 5],
    'student': ['Abbot', 'Doris', 'Emerson', 'Green', 'Jeames']
}
seat = pd.DataFrame(seat_data)

result = exchange_seats(seat)
print(result)
