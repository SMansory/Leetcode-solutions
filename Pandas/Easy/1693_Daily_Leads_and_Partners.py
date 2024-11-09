"""

Question: Daily leads and partners

Summary: For each 'date_id' and 'make_name', find the number of unique 'lead_ids' and 'partner_ids'.
Return the result table in any order.

Method: Group by 'date_id' and 'make_name', then use nunique to count distinct 'lead_id' and 'partner_id'.
Rename columns to 'unique_leads' and 'unique_partners'.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(["date_id", "make_name"], as_index = False).nunique().rename(columns = {"lead_id": "unique_leads", "partner_id": "unique_partners"})


# Example usage 
data = {'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'], 'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda', 'honda'], 'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2], 'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]} 
daily_sales = pd.DataFrame(data) 

result = daily_leads_and_partners(daily_sales) 
print(result)
