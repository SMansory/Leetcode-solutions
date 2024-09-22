"""

Question: Merge two sorted linked lists

Summary: Given the heads of two sorted linked lists 'list1' and 'list2', 
merge the two lists into one sorted list by splicing together the nodes of the first two lists. 
Return the head of the merged linked list.

Method: Use a dummy node to simplify the merging process. 
Iterate through both lists, comparing the current nodes and attaching the smaller node to the merged list. 
Continue until one of the lists is exhausted, then attach the remaining nodes from the other list.

Time complexity: O(n + m) where 'n' and 'm' are the lengths of the two lists.
Space complexity: O(1)
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to simplify the merging process
        head = dummy  # Pointer to build the new list
      
        while list1 and list2:
          
            if list1.val < list2.val:
                head.next = list1  # Attach the smaller node to the merged list
                list1 = list1.next  # Move to the next node in list1
              
            else:
                head.next = list2  # Attach the smaller node to the merged list
                list2 = list2.next  # Move to the next node in list2
              
            head = head.next  # Move to the next position in the merged list

        # Attach the remaining nodes from the non-exhausted list
        head.next = list1 or list2

        # Return the head of the merged list
        return dummy.next


# Example usage
result = Solution().mergeTwoLists([1, 2, 4], [1, 3, 4])
print(result)  # Output: [1, 1, 2, 3, 4, 4]
