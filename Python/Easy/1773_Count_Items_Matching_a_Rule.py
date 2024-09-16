"""

Question: Count items matching a rule

Summary: Given an array 'items' where each element is a list containing the type, color, and name of an item, 
and two strings 'ruleKey' and 'ruleValue', return the number of items that match the given rule. 
The rule matches if 'ruleKey' equals “type”, “color”, or “name” and 'ruleValue' matches the corresponding value in the item.

Method: Determine the index of the rule key in the list [“type”, “color”, “name”], 
then count how many items have the corresponding value equal to 'ruleValue'.

Time complexity: O(n), where n is the number of items.
Space complexity: O(n)
"""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Determine the index of the rule key
        ruleIndex = ["type", "color", "name"].index(ruleKey)
        # Create a list of values corresponding to the rule key
        ruleList = [item[ruleIndex] for item in items]
        # Count how many values match the rule value
        return ruleList.count(ruleValue)


# Example usage
result = Solution().countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                                 "color", "silver")
print(result)  # Output: 1
