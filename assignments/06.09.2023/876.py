class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        count=0
        while curr is not None:
            count+=1
            curr=curr.next
        result = head
        for i in range (count//2):
            result=result.next
        return result 