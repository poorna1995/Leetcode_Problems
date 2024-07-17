# def LinkedLIstNode():
#     data = "int(input('Enter data'))"
#     next = null


# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Example of creating a linked list node
# node = ListNode(10)
# print(node.data)  # Output: 10
# print(node.next)  # Output: None


# class LinkedList:
#     def __init__(self):
#         #  first value head and last value tail [ 1,2,3,4]
#         self.head=None # [] - empty head
     
# linkedlist=LinkedList()
# print(linkedlist.head.next)
    




class ListNode:
    def __init__(self,data):
        self.data= data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head= None
    
    def insert_data_beginning(self,data):
        new_node=ListNode(data)
        new_Node.next= self.head
        self.head= new_node
    
    def insert_data_end(self,data):
        new_node= ListNode(data)
        if self.head is None:
            self.head= new_node
            return
        current =self.head
        while current.next is not None:
            current= current.next
        current.next=new_node
    
    def print_list(self):
        current= self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print ('None')


#  1->3->8->9->None
# add 7  to given value at the 




        
linked_list = LinkedList()
linked_list.insert_data_end(10)
linked_list.insert_data_end(20)
linked_list.insert_data_end(30)
linked_list.print_list() 










    
    











