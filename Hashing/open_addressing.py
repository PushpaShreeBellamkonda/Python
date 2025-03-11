class myhash:
    def __init__(self,c):
        self.capacity=c
        self.table=[-1]*c
        self.size=0
    def hash(self,x):
        return x % self.capacity
    def search(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i] != -1:
            if t[i]==x:
                return True
            i=(i+1) % self.capacity
            if i==h:
                return False
        return False
    def insert(self,x):
        if self.size==self.capacity:
            return False
        if self.search(x)==True:
            return False
        t=self.table
        i=self.hash(x)
        if t[i] not in (-1,-2):
            i=(i+1)% self.capacity
        t[i]=x
        self.size=self.size+1
        return True
    def remove(self,x):
        h=self.hash(x)
        t=self.table
        i=h
        while t[i] != -1:
            if t[i]==x:
                t[i]=-2
                return True
            i=(i+1) % self.capacity
            if i==h:
                return False
        return False
    
h=myhash(7)
h.insert(22)
h.insert(41)
h.insert(65)
h.insert(52)
h.insert(25)
h.insert(78)
h.remove(65)
print(h.search(65))


