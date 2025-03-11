class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

def print_list(head):
    curr=head
    while curr!=None:
        print(curr.key,end=' ')
        curr=curr.next

def del_beg(head):
    curr=head
    if curr!=None:
        return curr.next
    else:
        return None
    
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=Node(50)
# print_list(head)
head=del_beg(head)
print_list(head)