def firstoc(l,x):
    for i in range(len(l)):
        if l[i]==x:
            return i
        
l=[10,20,20,40,50,60]
x=20
print(firstoc(l,x))

def lastoc(l,x):
    for i in reversed(range(len(l))):
        if l[i]==x:
            return i
        
l=[10,20,20,40,50,60]
x=20
print(lastoc(l,x))

def countoc(l,x):
    first=firstoc(l,x)
    last=lastoc(l,x)
    if first==-1:
        return 0
    else:
        return last - first +1
    
l=[10,20,20,40,50,60]
x=20
print(countoc(l,x))
