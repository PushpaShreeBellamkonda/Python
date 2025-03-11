class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printlist(head):
    curr=head
    while curr.next!=None:
        print(curr.key,end=" ")
        curr=curr.next

def sorted(head,x):
    curr=head
    temp=Node(x)
    if head==None:
        return temp
    elif x < curr.key:
        temp.next=head
        return temp

    else:
        while curr.next!=None and curr.next.key < x:
            curr = curr.next
        temp.next=curr.next
        curr.next=temp
        return head
    
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
print("list before insertion is ")
printlist(head)
print("list after insertion is:")
x=35
head=sorted(head,x)
printlist(head)


