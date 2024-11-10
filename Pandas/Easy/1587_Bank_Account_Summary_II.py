"""

Question: Bank account summary II

Summary: Write a function to report the name and balance of users with a balance higher than 10000. 
The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Method: Group the transactions by account and sum the amounts to get the account balance. 
Filter the accounts with a balance higher than 10000. Merge this result with the users table to get the names and balances.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # Group transactions by account and sum the amounts to get the balance
    accountBalance = transactions.groupby("account")["amount"].sum().reset_index(name = "balance")
    # Filter accounts with balance higher than 10000 and merge with users to get names
    return accountBalance[accountBalance["balance"] > 10000].merge(users, on = "account", how = "left")[["name", "balance"]]


# Example usage 
users_data = { 
  'account': [900001, 900002, 900003], 
  'name': ['Alice', 'Bob', 'Charlie'] 
} 
transactions_data = { 
  'trans_id': [1, 2, 3, 4, 5, 6, 7], 
  'account': [900001, 900001, 900001, 900002, 900003, 900003, 900003], 
  'amount': [7000, 7000, -3000, 1000, 6000, 6000, -4000], 
  'transacted_on': ['2020-08-01', '2020-09-01', '2020-09-02', '2020-09-12', '2020-08-07', '2020-09-07', '2020-09-11'] 
} 

users = pd.DataFrame(users_data) 
transactions = pd.DataFrame(transactions_data) 

result = account_summary(users, transactions)
print(result)
