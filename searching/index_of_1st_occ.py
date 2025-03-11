def bsearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]<x:
            low=mid+1
        elif l[mid]<x:
            high=mid-1
        else:
            if mid==0 or l[mid-1]!=l[mid]:
                return mid
            else:
                high=mid-1

    return -1

l=[10,20,20,40,50,60]
x=20
print(bsearch(l,x))

# naive solution

def firstoc(l,x):
    for i in range(len(l)):
        if l[i]==x:
            return i
        
l=[10,20,20,40,50,60]
x=20
print(firstoc(l,x))


