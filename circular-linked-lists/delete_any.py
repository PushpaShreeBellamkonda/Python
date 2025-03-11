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

def del_beg(head):
    if head is None:
        return None
    elif head.next==head:
        return None
    else:
        curr=head
        while curr.next!=head:
            curr=curr.next
        curr.next=head.next
        return curr.next

def del_any(head,x):
    if head is None:
        return head
    elif x==1:
        return del_beg(head)
    else:
        curr=head
        for i in range(x-2):
            curr=curr.next
        curr.next=curr.next.next
        return head
   
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head
printlist(head)
x=4
head=del_any(head,x)
printlist(head)