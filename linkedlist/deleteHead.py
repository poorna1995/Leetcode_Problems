def deleteNode(data):
    if head is None or head.next is None:
        return 
    else:
        head= head.next


# delete last nmoce= second last node
def deleteLastNode():
    if head is None: # nothing to delete
        return
    if head.next is None:
        head= None #  if there only one node
    
    slast=head
    while slast.next.next!=None:
        slast=slast.next
    
    slast.head=None


def deleteKeyNode(data):
    if head is None:
        return
    if head.next is None:
        head:None
    
    while head.next!= null:

        if head.next.data== key:
            head.next== head.next.next
            return
        head=head.next
        
    