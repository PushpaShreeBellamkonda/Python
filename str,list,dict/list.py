# avg of list
def avg_list(l):
    sum=0
    for x in l:
        sum=sum+x
    l=len(l)
    return sum/l

l=[3,5,6,7,4,9]
print(avg_list(l))




#even , odd

def even_odd(l):
    even=[]
    odd=[]
    for i in l:
        if i % 2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

l=[2,3,4,5,6,7,8,9]
even,odd=even_odd(l)
print(even)
print(odd)

# get smaller element 
def smaller(l,x):
    res=[]
    for i in l:
        if i < x:
            res.append(i)
    return res

l=[3,4,6,8,9,2,1]
x=6
print(smaller(l,x))

# sorting

def is_sort(l):
    i=1
    while i<len(l):
        if l[i] < l[i-1]:
            return False
        i+=1
    return True

l=[3,4,5,6,1]

if is_sort(l):
    print("True")
else:
    print("False")


# method 2

def is_sort(l):
   sl=sorted(l)
   if l == sl:
    return True
   else:
    return False

l=[3,4,5,6,1]

if is_sort(l):
    print("True")
else:
    print("False")


# find only odd

def oddval(l):
    res = 0
    for i in l:
        res = res ^ i
    return res

l=[20,20,10,10,10,30,30]
print(oddval(l))


# reverse a list

def revlist(l):
    s=0
    e=len(l)-1
    while s < e:
        l[s] , l[e] = l[e] , l[s]
        s+=1
        e-=1

l=[1,2,3,4,5,6]
revlist(l)
print(l)


# left rotate by one 
# method 1

l=[1,2,3,4]
l=l[1:] + l[0:1]
print(l)
# ,=method 1.1
l=[1,2,3,4]
l.append(l.pop(0))
print(l)

# method 2
def leftrot(l):
    x=l[0]
    n=len(l)
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x

l=[10,20,30,40,50]
leftrot(l)
print(l)

# left rotate by d times

# methos 1
l=[1,2,3,4,5,6,7]
d=2
l=l[d:] + l[:d]
print(l)

# method 2

from collections import deque
l=[1,2,3,4,5,6,7]
d=2
dq=deque(l)
dq.rotate(-d)
l=list(dq)
print(l)


# count distinct elements in a list

def distinct(l):
    res=1
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res+=1
    return res

l=[10,20,30,10,20,30]
print(distinct(l))

# method 2

def distinct(l):
    s=set(l)
    return len(s)
l=[10,20,30,10,20,30]
print(distinct(l))







        