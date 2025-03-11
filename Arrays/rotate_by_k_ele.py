from collections import deque
def rotate_k(arr,k):
    d=deque(arr)
    d.rotate(k)
    return list(d)
arr=list(map(int,input("enter the values").split()))
k=2
print(rotate_k(arr,k))