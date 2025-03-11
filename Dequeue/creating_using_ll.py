class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
        self.prev=None

class dequeue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.sz=0

    def size(self):
        return self.sz
    
    def isempty(self):
        return (self.sz==0)
    
    def insertRear(self,x):
        temp=Node(x)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
            temp.prev=self.rear
        self.rear=temp
        self.sz+=1

    def deleteFront(self):
        if self.front==None:
            return None
        else:
            res=self.front.key
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            else:
                self.front.prev=None
            self.sz-=1
            return res
        
q=dequeue()
q.insertRear(10)
q.insertRear(20)
q.insertRear(30)
q.insertRear(40)
print(q.deleteFront())
print(q.size())
print(q.isempty())