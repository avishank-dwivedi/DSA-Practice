class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head , n):
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for _ in range (n + 1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
new_head = s.removeNthFromEnd(head, 2)
