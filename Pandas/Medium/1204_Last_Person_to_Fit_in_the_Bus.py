"""

Question: Last person to fit in the bus

Summary: Write a function that determines the name of the last person who can board a bus without the total weight exceeding 1000 kilograms. 
The function processes the queue of people based on their turn order.

Method: First, sort the 'queue' DataFrame by the 'turn' column. Then calculate the cumulative sum of the weights.
Identify the last person whose cumulative weight, including their own, does not exceed 1000 kilograms.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    # Sort by 'turn' order
    queue = queue.sort_values(by='turn')
    # Calculate the cumulative sum of the weights
    queue['weight'] = queue['weight'].cumsum()
    # Return the last person's name that can board without exceeding weight limit
    return queue[queue['weight']<= 1000].tail(1)[['person_name']]


# Example usage
queue_data = {
    'person_id': [5, 4, 3, 6, 1, 2],
    'person_name': ['Alice', 'Bob', 'Alex', 'John Cena', 'Winston', 'Marie'],
    'weight': [250, 175, 350, 400, 500, 200],
    'turn': [1, 5, 2, 3, 6, 4]
}
queue = pd.DataFrame(queue_data)

result = last_passenger(queue)
print(result)
