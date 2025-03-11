class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printlist(head):
    curr=head
    while curr is not None:
        print(curr.key,end=" ")
        curr=curr.next

def revlist(head):
    stack=[]
    curr=head
    while curr is not None:
        stack.append(curr.key)
        curr=curr.next
    curr=head
    while curr is not None:
        curr.key=stack.pop()
        curr=curr.next
    return head

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
print("before reversing")
printlist(head)
print("\nafter reversing")
head=revlist(head)
printlist(head)