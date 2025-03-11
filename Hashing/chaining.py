class myhash:
    def __init__(self,b):
        self.size=b
        self.table=[[] for x in range(b)]
    def insert(self,x):
        i= x % self.size
        self.table[i].append(x)
    def remove(self,x):
        i=x % self.size
        if x in self.table[i]:
            self.table[i].remove(x)
    def search(self,x):
        i=x % self.size
        return x in self.table[i]
    
h=myhash(7)
h.insert(22)
h.insert(41)
h.insert(65)
h.insert(52)
h.insert(25)
h.insert(78)
h.remove(65)
print(h.search(65))