from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        ml = []
        mll = ListNode(-1,None)

        while (pointer1 != None or pointer2 != None):
            if(pointer1 == None):
                ml.append(pointer2.val)
                pointer2 = pointer2.next
            elif(pointer2 == None):
                ml.append(pointer1.val)
                pointer1 = pointer1.next
            elif(pointer1.val > pointer2.val):
                ml.append(pointer2.val)
                pointer2 = pointer2.next
            else:
                ml.append(pointer1.val)
                pointer1 = pointer1.next
        
        llp  = mll
        for e in ml:
            node = ListNode(e, None)
            llp.next = node
            llp = llp.next
        return mll.next
    


               