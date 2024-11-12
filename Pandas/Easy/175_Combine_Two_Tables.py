"""

Question: Combine two tables

Summary: Write a function to report the first name, last name, city, and state of each person in the 'Person' table.
If the address of a 'personId' is not present in the 'Address' table, report null instead. Return the result table in any order.

Method: Use the 'merge' method in pandas to join the 'Person' and 'Address' tables on 'personId',
using a left join to include all persons. 
Select the columns 'firstName', 'lastName', 'city', and 'state' from the merged DataFrame.

Time complexity: O(n)
Space complexity: O(n)
"""

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Merge the 'Person' and 'Address' tables on 'personId' using a left join and select the required columns
    return person.merge(address, on = "personId", how = "left")[["firstName", "lastName", "city", "state"]]


# Example usage
person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}

person = pd.DataFrame(person_data)
address = pd.DataFrame(address_data)

result = combine_two_tables(person, address)
print(result)
