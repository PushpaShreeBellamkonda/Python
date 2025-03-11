class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def search(head,x):
    curr=head
    pos=1
    while curr!=None:
        if curr.key==x:
            return pos
        pos+=1
        curr=curr.next
    return -1

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
x=20
print(search(head,x))
       

