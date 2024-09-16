"""

Question: Middle of the Linked List

Summary: Given the head of a singly linked list, return the middle node. 
If there are two middle nodes, return the second one.

Method: Use two pointers, 'slow' and 'fast'. Move 'slow' one step at a time and 'fast' two steps at a time.
When 'fast' reaches the end, 'slow' will be at the middle node.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
          
        return slow


# Example usage
result = Solution().middleNode([1, 2, 3, 4, 5])
print(result)  # Output: [3, 4, 5]
