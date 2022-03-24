#Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1=head
        count=0
        p2=head
        nodcnt=1
        flag=False
        while p1.next:
            if count == n:
                flag = True
            if flag == False:
                p1=p1.next
                count+=1
                # print(f'count={count},p1={p1.val}')
            else:
                p1=p1.next
                p2=p2.next
                print(f'p1={p1.val},p2={p2.val}')
            nodcnt+=1
        print(p2.val,nodcnt)
        if nodcnt == n:
            head=head.next
            return head
        p2.next=p2.next.next
        return head