from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        n = head
        while n:
            s.append(n.val)
            n=n.next

        n = head
        while n:
            v = s.pop()
            if(v != n.val):
                return False
            n=n.next
        
        return True

head = [1,2,2,1]

#head = [1,2]
    
l1 = ListNode(-1, None)
head1 = l1
for e in head:
    next = ListNode(e, None)
    l1.next = next
    l1 = l1.next
l1 = head1.next


print(Solution.isPalindrome(Solution, l1))
