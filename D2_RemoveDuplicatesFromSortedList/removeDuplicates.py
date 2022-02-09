class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        ptr=head
        while ptr != None and ptr.next!=None:
            if ptr.val == ptr.next.val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
            print(ptr.val)
        return dummy
