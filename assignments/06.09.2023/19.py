class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr=head
        count = 0
        while curr is not None:
            count+=1
            curr=curr.next
        curr=head
        if (count-n)==0:
            return head.next
        for i in range (count-n-1):
            curr=curr.next
        curr.next=curr.next.next
        return head
           