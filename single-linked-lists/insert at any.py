class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

def insertatany(head,pos,key):
    temp = Node(key)
    if pos == 1:
        temp.next = head
        return temp
    
    curr = head
    for i in range(pos-2):
        curr=curr.next
        if curr == None:
            return head
    
    temp.next = curr.next
    curr.next = temp
    return head

def printlist(head):
    curr=head
    while curr!= None:
        print(curr.key , end= " ")
        curr = curr.next

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)   

print("Original List:")
printlist(head)

head = insertatany(head,3,25)

print("\n Modified List After Insertions:")
printlist(head)
