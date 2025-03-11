class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printlist(head):
    if head is None:
       return
    print(head.key,end=" ")
    curr=head.next
    while curr!=head:
        print(curr.key,end=" ")
        curr=curr.next
    print()

def insert_any(head,x):
    temp=Node(x)
    if head is None:
        temp.next=temp
        return temp
    else:
        curr=head
        while curr.next!=head:
            curr=curr.next
        curr.next=temp
        temp.next=head
        return head
    
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head
printlist(head)
x=50
head=insert_any(head,x)
printlist(head)
