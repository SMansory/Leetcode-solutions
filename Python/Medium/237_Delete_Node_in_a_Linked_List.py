"""

Question: Delete node in a linked list

Summary: Given a node in a singly-linked list, delete the node. You will not have access to the first node of the list.
The values of the linked list are unique, and the given node is not the last node in the linked list.

Method: To delete the node, copy the value of the next node to the current node and then delete the next node.

Time complexity: O(1)
Space complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteNode(self, node):
        head = None
      
        while node and node.next:
            node.val = node.next.val
            head = node
            node = node.next
        
        if head:
            head.next = None
        
