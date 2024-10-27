"""

Question: Palindrome linked list

Summary: Given the head of a singly linked list, determine if it is a palindrome. 
Return true if it is, and false otherwise.

Method: Traverse the linked list to create a string representation of the list's values. 
Check if the string is a palindrome by comparing it to its reverse.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = ""
        lst = head
        while lst:
            s += str(lst.val)
            lst = lst.next
        if s == s[::-1]:
            return True
        return False


# Example usage
result = Solution().isPalindrome([1, 2, 2, 1])
print(result)  # Output: true
