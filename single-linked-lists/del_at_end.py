class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printlist(head):
    curr=head
    while curr!=None:
        print(curr.key,end=" ")
        curr=curr.next

def delend(head):
    curr=head
    if curr==None:
        return None
    if curr.next==None:
        return None
    if curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head

head=Node(10)
head.next=Node(20)
head.next.next=Node(40)
delend(head)
printlist(head)



