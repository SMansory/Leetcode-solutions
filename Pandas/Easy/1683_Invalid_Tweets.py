"""

Question: Invalid tweets

Summary: Write a function to find the 'IDs' of the invalid tweets. 
A tweet is considered invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Method: Use the 'str.len' method to check the length of the content and 
filter rows where the length is greater than 15 characters. Return the 'tweet_id' of these rows.

Time complexity: O(n)
Space complexity: O(1)
"""

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter tweets with content length greater than 15
    return tweets.loc[tweets["content"].str.len() > 15, ["tweet_id"]]


# Example usage
data = {
    'tweet_id': [1, 2],
    'content': ['Let us Code', 'More than fifteen chars are here!']
}
tweets = pd.DataFrame(data)

result = invalid_tweets(tweets)
print(result)
