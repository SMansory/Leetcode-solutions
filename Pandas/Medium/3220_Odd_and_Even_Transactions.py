"""

Question: Odd and even transactions

Summary: Write a function that calculates the sum of amounts for odd and even transactions for each day.
If there are no odd or even transactions for a specific date, it displays as 0. 
Return the result ordered by 'transaction_date' in ascending order.

Method: Assign new columns 'odd_sum' and 'even_sum' to the transactions DataFrame by applying a lambda function that 
sets 'odd_sum' for odd amounts and 'even_sum' for even amounts. Group the DataFrame by 'transaction_date' and 
sum the values of 'odd_sum' and 'even_sum'. Sort the result by 'transaction_date'.

Time complexity: O(n) 
Space complexity: O(n) 
"""

import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    # Assign 'odd_sum' and 'even_sum' columns based on the amount
    return (transactions
    .assign(odd_sum = transactions['amount'].apply(lambda x: x if x % 2 == 1 else 0), even_sum = transactions['amount'].apply(lambda x: x if x % 2 == 0 else 0))
    # Group by 'transaction_date' and sum the values of 'odd_sum' and 'even_sum'f        
    .groupby('transaction_date')
    [['odd_sum', 'even_sum']]
    .sum()
    # Sort the result by 'transaction_date'         
    .sort_values('transaction_date')
    .reset_index())


# Example usage
transactions_data = {
    'transaction_id': [1, 2, 3, 4, 5, 6],
    'amount': [150, 200, 75, 300, 50, 120],
    'transaction_date': ['2024-07-01', '2024-07-01', '2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03']
}
transactions = pd.DataFrame(transactions_data)

result = sum_daily_odd_even(transactions)
print(result)
