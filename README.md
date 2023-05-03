Repo for leetcode solutions while learning python.


Helpful bits
    Imports
        from typing import Optional
        from typing import List

    Linked List builder
        head = [1,1,1]

        l1 = ListNode(-1, None)
        head1 = l1
        for e in head:
            next = ListNode(e, None)
            l1.next = next
            l1 = l1.next
        l1 = head1.next

    Tree builder
        def build(i, r):
            if(i >= len(r) or r[i] == None):
                return None
            a = TreeNode(r[i], None, None)
            a.left = build(i+1, r)
            a.right = build(i+2, r)
            return a

        p1 = [1,2,3]

        p = build(0, p1)
