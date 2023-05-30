# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while(head.next):
            num=num*2+ head.next.val
            head = head.next
        return num




head = [1,0,1]
head = [0]

l1 = ListNode(-1, None)
head1 = l1
for e in head:
    next = ListNode(e, None)
    l1.next = next
    l1 = l1.next
l1 = head1.next

print(Solution.getDecimalValue(Solution, l1))