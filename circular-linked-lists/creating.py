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

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head
printlist(head)
