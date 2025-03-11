class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.sz=0

    def size(self):
        return self.sz
    
    def isempty(self):
        return (self.sz==0)
    
    def getFront(self):
        return self.front.key
    
    def getRear(self):
        return self.rear.key
    
    def enqueue(self,x):
        temp=Node(x)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.sz+=1

    def dequeue(self):
        if self.front==None:
            return None
        else:
            res=self.front.key
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.sz-=1
            return res
        
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.dequeue())
print(q.size())
print(q.isempty())
print(q.getFront())
print(q.getRear())