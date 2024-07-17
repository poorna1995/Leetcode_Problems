array=[0,1,2,3]
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=next

class Solution:
    def reverseLinkedList(head=ListNode(array)):
        current=head
        prev=None
        next=None
        while current:
            next= current.next
            current.next=prev
            prev=current
            current=next
        return prev


print(Solution().reverseLinkedList(array))


        