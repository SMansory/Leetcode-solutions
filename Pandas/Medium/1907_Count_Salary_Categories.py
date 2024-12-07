"""

Question: Count salary categories

Summary: Write a function that calculates the number of bank accounts in three salary categories:
"Low Salary" (less than $20000), "Average Salary" (between $20000 and $50000 inclusive), 
and "High Salary" (greater than $50000). The result should includes all three categories, 
with a count of zero for any category with no accounts.

Method: Filter the 'accounts' DataFrame into three categories based on the 'income' column. 
Count the number of accounts in each category. Create a new DataFrame with the category names and their respective counts.

Time complexity: O(n) 
Space complexity: O(n)
"""

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Count high salary accounts
    high_salary = accounts[accounts["income"] > 50000].shape[0]
    # Count low salary accounts
    low_salary = accounts[accounts["income"] < 20000].shape[0]
    # Count average salary accounts
    average_salary = accounts[(accounts["income"] >= 20000) & (accounts["income"] <= 50000)].shape[0]
    # Create a DataFrame with the counts of each salary category
    salary_catagories_count = pd.DataFrame({
        "category": ["High Salary", "Low Salary", "Average Salary"],
        "accounts_count": [high_salary, low_salary, average_salary]
    })
    return salary_catagories_count


# Example usage
accounts_data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796]
}
accounts = pd.DataFrame(accounts_data)

result = count_salary_categories(accounts)
print(result)
