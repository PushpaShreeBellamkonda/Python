class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def printlist(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()

def insert_at_beg(head,x):
    temp3=Node(x)
    if head.prev==None:
        head.prev=temp3
        temp3.next=head
        return temp3

head=Node(10)
temp1=Node(20)
temp2=Node(30)
head.next=temp1
temp1.prev=head
temp1.next=temp2
temp2.prev=temp1
printlist(head)
x=5 
head=insert_at_beg(head,x)
printlist(head)