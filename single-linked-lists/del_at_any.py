class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printlist(head):
    curr=head
    while curr.next!=None:
        print(curr.key,end=" ")
        curr=curr.next

def delany(head,pos):
    temp=head
    prev=None

    if temp==None:
        return head
    if pos==1:
        head=temp.next
        return head
    
    for i in range(1,pos):
        prev=temp
        temp=temp.next
        if temp is None:
            print("data not present")
        else:
            prev.next=temp.next
        return head

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
print("original list is " , end=' ')
printlist(head)
pos=2
head=delany(head,pos)
print("list after deletion" , end=" ")
printlist(head)

