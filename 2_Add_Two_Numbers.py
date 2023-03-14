from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        o = ListNode(-1, None)
        headO = o

        while(l1 or l2):
            if(l1 != None):
                d1 = l1.val
            else:
                d1 = 0
            if(l2 != None):
                d2 = l2.val
            else:
                d2 = 0
            

            digit = carry + d1 + d2
            carry = int(digit/10)
            digit %= 10

            o.next = ListNode(digit, None)
            o = o.next
            
            if(l1 != None):
                l1 = l1.next
            if(l2 != None):
                l2 = l2.next

            print(digit)
        
        if(carry != 0 ):
            o.next = ListNode(carry, None)
            print("add a final node for carry")
            
        return headO.next
    
a =[9,9,9,9,9,9,9]
b = [9,9,9,9]

l1 = ListNode(-1, None)
head1 = l1
for e in a:
    next = ListNode(e, None)
    l1.next = next
    l1 = l1.next
l1 = head1.next

l2 = ListNode(-1, None)
head2 = l2
for e in b:
    next = ListNode(e, None)
    l2.next = next
    l2 = l2.next
l2 = head2.next

output = Solution.addTwoNumbers(Solution, l1, l2)

while(output):
    print(output.val)
    output = output.next

#print(head.next.val)