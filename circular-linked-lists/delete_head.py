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

# def del_head(head):
#     if head is None:
#         return None
#     elif head.next==head:
#         return None
#     curr=head
#     while curr.next!=head:
#         curr=curr.next
#     curr.next=head.next
#     return curr.next

def del_head(head):
    if head is None:
        return None
    elif head.next==head:
        return None
    else:
        head.key=head.next.key
        head.next=head.next.next
        return head
    
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head
printlist(head)
head=del_head(head)
printlist(head)
