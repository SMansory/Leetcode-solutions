"""

Question: Same tree

Summary: Given the roots of two binary trees 'p' and 'q', write a function to check if they are the same. 
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Method: Convert both trees to their string representations and compare the strings.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Convert both trees to their string representations and compare
        return str(p) == str(q)


# Example usage
result = Solution().isSameTree([1, 2, 3], [1, 2, 3])
print(result)  # Output: true
