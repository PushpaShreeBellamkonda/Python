from collections import deque
def rotate_right(arr,k):
    r=deque(arr)
    r.rotate(k)
    return list(r)

def rotate_left(arr,k):
    l=deque(arr)
    l.rotate(-k)
    return list(l)

arr=list(map(int,input("eneter the values: ").split()))
k=int(input("enter k value: "))
direction=input("enter the direction: ")
if direction =="right":
    print(rotate_right(arr,k))
else:
    print(rotate_left(arr,k))