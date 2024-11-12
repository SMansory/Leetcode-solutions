"""

Question: Article views I

Summary: Write a function to find all the authors that viewed at least one of their own articles. 
Return the result table sorted by 'id' in ascending order.

Method: Filter the DataFrame to include only rows where 'author_id' is equal to 'viewer_id'. 
Rename the 'author_id' column to 'id' and drop duplicate rows based on 'id'. Sort the result by 'id' in ascending order.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where 'author_id' is equal to 'viewer_id' 
    views = views[views["author_id"] == views["viewer_id"]].rename(columns = {"author_id": "id"}).drop_duplicates("id")
    # Return the sorted result
    return views[["id"]].sort_values("id")


# Example usage
data = {
    'article_id': [1, 1, 2, 2, 4, 3, 3],
    'author_id': [3, 3, 7, 7, 7, 4, 4],
    'viewer_id': [5, 6, 7, 6, 1, 4, 4],
    'view_date': [
        '2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02',
        '2019-07-22', '2019-07-21', '2019-07-21'
    ]
}
views = pd.DataFrame(data)

result = article_views(views)
print(result)
