# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]



head = [1,2,3,4,5]
head = [1,2,3,4,5,6]

l1 = ListNode(-1, None)
head1 = l1
for e in head:
    next = ListNode(e, None)
    l1.next = next
    l1 = l1.next
l1 = head1.next


print(Solution.middleNode(Solution, l1))