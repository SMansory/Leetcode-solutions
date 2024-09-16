"""
Question: Find the center of a star graph

Summary: Given an undirected star graph with 'n' nodes labeled from 1 to 'n',
and a 2D integer array 'edges' where each 'edges[i] = [ui, vi]' indicates an edge between nodes 'ui' and 'vi',
return the center of the star graph. A star graph has one center node connected to every other node with exactly 'n - 1' edges.

Method: Check the first two edges to determine the common node, which is the center.

Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Check the first two edges to determine the common node
        return edges[0][0] if (edges[0][0] == edges[1][0]) or (edges[0][0] == edges[1][1]) else edges[0][1]


# Example usage
result = Solution().findCenter([[1, 2],[2, 3],[4, 2]])
print(result)  # Output: 2
