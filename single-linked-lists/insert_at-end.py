class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def insert_at_end(head,key):
    temp=Node(key)
    curr=head
    while curr.next:
         curr=curr.next
    curr.next=temp
    return head 
       
def printlist(head):
        curr=head
        while curr!=None:
            print(curr.key,end=" ")
            curr=curr.next
    

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

print("Original List:")
printlist(head)


head=insert_at_end(head,1)
head=insert_at_end(head,2)

print("Modified List After Insertions:")
printlist(head)


    




