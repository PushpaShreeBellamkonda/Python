class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def insert_at_beg(head,key):
    temp=Node(key)
    temp.next=head
    return temp
    
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


head=insert_at_beg(head,1)
head=insert_at_beg(head,2)

print("\n Modified List After Insertions:")
printlist(head)


    




