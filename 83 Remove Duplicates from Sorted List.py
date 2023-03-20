from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        
        # n = head
        # while n:
        #     print(n.val)
        #     n=n.next
        
        n=head.next
        prev = head

        while n:
            if(n.val == prev.val):
                prev.next = n.next
                n = prev.next
            else:
                prev = n 
                n = n.next


        n = head
        while n:
            print(n.val)
            n=n.next
        
        return head
    


head = [1,1,1]
#head = [1,1,2,3,3]

l1 = ListNode(-1, None)
head1 = l1
for e in head:
    next = ListNode(e, None)
    l1.next = next
    l1 = l1.next
l1 = head1.next

Solution.deleteDuplicates(Solution, l1)