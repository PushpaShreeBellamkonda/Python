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

def del_at_end(head):
    if head==None:  
        return None
    if head.next==None:
        return None
    else:
        curr=head
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        return head

head=Node(10)
temp1=Node(20)
temp2=Node(30)
head.next=temp1
temp1.prev=head
temp1.next=temp2
temp2.prev=temp1
printlist(head)
head=del_at_end(head)
printlist(head)
