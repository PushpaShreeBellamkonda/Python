import math
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.head=None
        self.sz=0

    def push(self,x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.sz=self.sz+1

    def size(self):
        return self.sz
    
    def pop(self):
        if self.head==None:
            return math.inf
        res=self.head.data
        self.head=self.head.next
        self.sz=self.sz-1
        return res
    
    def peek(self):
        if self.head==None:
            return math.inf
        return self.head.data
    
    def print_stack(self,head):
        curr=self.head
        while curr!=None:
            print(curr.key,end=" ")
            curr=curr.next
                    
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
print(s.pop())
print(s.peek())
print(s.size())

