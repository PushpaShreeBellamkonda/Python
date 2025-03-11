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

def inser_at_end(head,x):
    temp=Node(x)
    curr=head
    if head==None:
        return temp
    else:
        while curr.next!=None:
            curr=curr.next
        curr.next=temp 
        temp.prev=curr
        return head 

head=Node(10)
temp1=Node(20)
temp2=Node(30)
head.next=temp1
temp1.prev=head
temp1.next=temp2
temp2.prev=temp1
printlist(head)
x=40
head=inser_at_end(head,x)
printlist(head)