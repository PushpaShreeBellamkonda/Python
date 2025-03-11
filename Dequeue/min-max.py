from collections import deque
class mydeque:
    def __init__(self):
        self.dq=deque()

    def insertMin(self,x):
        self.dq.appendleft(x)
    
    def insertMax(self,x):
        self.dq.append(x)

    def extractMin(self):
        return self.dq.popleft()
    
    def extractMax(self):
        return self.dq.pop()
    
    def getMin(self):
        return self.dq[0]
    
    def getMax(self):
        return self.dq[-1]
    
d=mydeque()
d.insertMin(10)
d.insertMin(5)
d.insertMax(20)
d.insertMax(30)
print(d)
print(d.extractMin())
print(d.extractMax())
print(d.getMin())
print(d.getMax())